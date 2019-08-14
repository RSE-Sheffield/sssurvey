#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

# Get details for plots from look up table
from column_name_renaming import col_shortener
from column_name_renaming import sort_no_further_analysis
from column_name_renaming import yes_no_analysis
from column_name_renaming import add_an_other_category
from column_name_renaming import scale_analysis
from column_name_renaming import worded_scale_analysis
from bivariate_instructions import which_by_which


DATAFILELOC = "./data/"
DATAFILENAME = "Cleaning-of-Uni-Soton-Software-Survey-26Jun19.csv"
CSVSTORE = "./output_csv/"
BIVARIATESTORE = "./output_csv/bivariate/"


def import_csv_to_df(location, filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(location + filename)


def export_to_csv(df, location, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(location + filename + '.csv', index=index_write)


def remove_timestamp(df):
    """
    We don't need the Timestamp col in the analysis but it is nice to have it in the data (in case people want to see
    how responses came in. Hence I can't remove it in the cleaning stage completed before this analysis, but I'll remove
    it now.
    :param df: the main df containing all the data
    :return: the main df, but without a Timestamp col
    """

    df.drop(labels=['Timestamp'], axis='columns', inplace=True)

    return df


def clean_col_names(df):
    """
    Takes a dict from a look up file and uses it to rename the columns
    to something shorter and tidier
    :param df: the main df
    :return: the main df with new col names
    """

    return df.rename(index=str, columns=col_shortener)


def shorten_faculties(df):
    """
    There's no need to have "Faculty of" before each faculty name in the output data. It just makes it clunky
    so removing it here.
    :param df: the main df
    :return: the main df with "Faculty of " removed from "faculty" col
    """

    df['faculty'].replace(regex=True, inplace=True, to_replace=r'Faculty of ', value=r'')

    return df


def get_counts(df):
    """
    Get summary dataframes. Where needed split up the multiple answer responses so that they fall into simple bins.
    :param df: the main df
    :return: dict of dfs holding summaries on the answers to each question
    """

    # Initialise a dict into which I shall store the results dfs
    summary_dfs = {}

    # Go through each col, get the counts of each question, calculate a percentage and then store as a result df
    for current_col in df.columns:
        df_counts = pd.DataFrame(data = (df[current_col].value_counts(sort=False)), columns = [current_col])
        # Shift the index into a new column needed for the next bit
        df_counts['answers'] = df_counts.index
        # Multi-choice questions provide multiple answers separated by semicolon. Need to separate these up and count
        # them individually. The method I use (with Stack etc) below fails on answers that are numeric, so I filter them
        # out. Obviously, anything with a semicolon in it is not numeric!
        if df_counts['answers'].dtype == 'object':
            df_counts = (df_counts.set_index(current_col)['answers'].str.split(';', expand=True).stack().reset_index(name='answers').groupby('answers', as_index=False)[current_col].sum())
        df_counts.set_index('answers', inplace=True)
        df_counts['percentage'] = round(100 * df_counts[current_col] / df_counts[current_col].sum(), 0)
        # Save as dict of dfs
        summary_dfs[current_col] = df_counts

    return summary_dfs


def clean_software_funding(summary_dfs):
    """
    Removes the 'No (I\'m not involved in writing funding proposals)' answer from the question on whether people have
    applied for software funding. In a perfect world, this would have been removed in the pre-analysis data cleaning in
    OpenRefine, but that's not possible, because this is a multiple choice question that separates multiple answers
    with semi-colons and OpenRefine can't handle that. The get_counts function deals with the semicolon problem, so now
    we can finish cleaning the data.
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: dict of dfs holding summaries on the answers to each question - but with the funding question cleaned so
            people who do not write bids are not included.
    """

    key = 'funds_for_development'

    df_temp = summary_dfs[key]
    df_temp.drop(index='No (I\'m not involved in writing funding proposals)', inplace=True)
    # Obviously, removing one of the options changes the percentages, so have to re-do that calculation
    df_temp['percentage'] = round(100 * df_temp[key] / df_temp[key].sum(), 0)

    return summary_dfs


def change_lows_to_other(summary_dfs):
    """
    Questions with an "other" response can generate lots of low value responses. Convert all answers that gain fewer
     than 5 responses into an "other" category to make things cleaner.
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: dict of dfs holding summaries on the answers to each question - but with an other response used to mop up
             answers with low response numbers
    """

    for key in add_an_other_category:
        df_temp = summary_dfs[key]
        # New index makes the current index a col that we can work with
        df_temp.reset_index(inplace=True)
        # Make a Boolean mask of all the rows that have fewer than 5 responses and use it
        # to change the category to 'other'
        mask = df_temp[key].le(5)
        df_temp.loc[mask, 'answers'] = 'other'
        # Collapse all the 'other' rows into a single row, sum the result and convert back to a df
        df_temp = pd.DataFrame(df_temp.groupby('answers')[key].sum())
        df_temp.columns = [key]
        # Add a percentage col, because the last one was stripped by the groupby operation
        df_temp['percentage'] = round(100 * df_temp[key] / df_temp[key].sum(), 0)
        # Replace the original df in the dict of dfs
        summary_dfs[key] = df_temp

    return summary_dfs


def find_number_responses(summary_dfs, df):
    """
    Finds the number of people who responded to each question and saves it as a csv
    :param df: the main dataframe
    :return: nothing
    """

    response_list = {}

    for key in summary_dfs:
        df_temp = summary_dfs[key]
        response_list[key] = df_temp[key].sum()

    # This approach doesn't work for multiple choice questions (you get over-counting for anyone that added more than
    # one response. For these questions, to get the response number we must go back to the original df

    multi_questions = ['funders', 'funds_for_development']

    for current_question in multi_questions:
        df_temp = df.dropna(axis=0, subset=[current_question])
        # Write the actual number of responses over the current number in the response list
        response_list[current_question] = len(df_temp)

    df_responses = pd.DataFrame(response_list.items(), columns=['answers', 'responses'])

    export_to_csv(df_responses, CSVSTORE, 'responses', False)

    return


def sort_and_save(summary_dfs):
    """
    Takes the summary dfs that merely need sorted. Uses info from the sort_no_further_analysis var to know which dfs to
    process
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: a better ordered dict of dfs holding summaries on the answers to each question
    """

    for key in sort_no_further_analysis:
        df_temp = summary_dfs[key]
        df_temp.sort_values(by=key, inplace=True, ascending=False)
        # Replace the original df in the dict of dfs
        summary_dfs[key] = df_temp

    return summary_dfs


def yes_and_no(summary_dfs):
    """
    Takes summary dfs of yes-and-no questions, sorts them yes first, then no. Uses the yes_no_analysis var to work out
    which dfs to process
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: a better ordered dict of dfs holding summaries on the answers to each question
    """

    for key in yes_no_analysis:
        df_temp = summary_dfs[key]
        # Sorting an index of 'yes' and 'no' in descending order is the same as ensuring that yes comes first
        # which is... you know... what I want
        df_temp.sort_index(inplace=True, ascending=False)
        # Replace the original df in the dict of dfs
        summary_dfs[key] = df_temp

    return summary_dfs


def scale_question_analysis(summary_dfs):
    """
    To make plotting easy, this sorts the questions with a 1 to 5 answer scale, and saves them back into the dict of
    dfs.
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: a better ordered dict of dfs holding summaries on the answers to each question
    """

    for key in scale_analysis:
        df_temp = summary_dfs[key]
        df_temp.sort_index(ascending=True, inplace=True)
        # Replace the original df in the dict of dfs
        summary_dfs[key] = df_temp

    return summary_dfs


def scale_worded_questions(summary_dfs):

    """
    Some questions have wordy answers that I want to present in a particular order. This puts them in that order using
    a categorical. I feel that there must be an easier way of doing this, but I can't find it. The function saves the
    re-ordered dfs back in the summary-dfs.
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: a better ordered dict of dfs holding summaries on the answers to each question
    """

    for key in worded_scale_analysis:
        df_temp = summary_dfs[key]
        # New index makes the current index a col that we can work with
        df_temp.reset_index(inplace=True)

        if key in ['version_control', 'continuous_integration', 'unit_testing']:
            # These categoricals allow you to order a column based on a list. Seems long winded, but it was the only
            # straightforward way I could find to do it.
            df_temp['answers'] = pd.Categorical(df_temp['answers'],
                                                categories=['Not heard of it', 'Not confident','Confident',
                                                            'Very confident'], ordered=True)
            df_temp.sort_values('answers', inplace=True)

        elif key == 'funds_for_development':
            df_temp['answers'] = pd.Categorical(df_temp['answers'],
                                                categories=['Yes',
                                                    'No (but we DID expect to write software as part of the project)',
                                                    'No (we did NOT expect to write software as part of the project)'],
                                                ordered=True)
            df_temp.sort_values('answers', inplace=True)

        elif key in ['hire_full_time_developer', 'hire_rse']:
            df_temp['answers'] = pd.Categorical(df_temp['answers'],
                                                categories=['Perfect', 'Suitable', 'Unsuitable'], ordered=True)
            df_temp.sort_values('answers', inplace=True)

        # Now that the hard work's done, we can set the answers col back to be the index and save back into the dict
        # of dfs
        df_temp.set_index('answers', inplace=True)
        summary_dfs[key] = df_temp

    return summary_dfs


def bivariate_analysis(df, summary_dfs):

    """
    Conducts bivariate analysis as instructed by the imported which_by_which
    dict. Each key in the dict is one question from the survey which will be segmented
    by the question(s) held in the value(s) of the dict.
    :param df:
    :param summary_dfs:
    :return:
    """
    counter = 0

    for denominator in which_by_which:
        differentiator = list(summary_dfs[denominator].index)
        counter += 1
        for current_diff in differentiator:
            temp_df=df[df[denominator]==current_diff]
            for current_question in which_by_which[denominator]:
                df_counts = pd.DataFrame(data=(temp_df[current_question].value_counts(sort=False)), columns=[current_question])
                df_counts['answers'] = df_counts.index
                # Multi-choice questions provide multiple answers separated by semicolon. Need to separate these up and count
                # them printindividually. The method I use (with Stack etc) below fails on answers that are numeric, so I filter them
                # out. Obviously, anything with a semicolon in it is not numeric!
                # Needs an "and length isn't 0" bit because the function doesn't work for zero-length dfs
                if df_counts['answers'].dtype == 'object' and len(df_counts) != 0:
                    df_counts = (
                        df_counts.set_index(current_question)['answers'].str.split(';', expand=True).stack().reset_index(
                            name='answers').groupby('answers', as_index=False)[current_question].sum())
                df_counts.set_index('answers', inplace=True)
                df_counts['percentage'] = round(100 * df_counts[current_question] / df_counts[current_question].sum(), 0)
                filename = str(counter) + "_sep_" + str(current_diff) + "_sep_" + str(current_question) + '_' + str(denominator)
                export_to_csv(df_counts, BIVARIATESTORE, filename, True)
    return


def write_out_summaries(summary_dfs):
    """
    Write the summary dfs out to csvs
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: nothing
    """

    for key in summary_dfs:
        export_to_csv(summary_dfs[key], CSVSTORE, key, True)

    return


def main():
    """
    Main function to run program
    """

    df = import_csv_to_df(DATAFILELOC, DATAFILENAME)

    df = remove_timestamp(df)

    df = clean_col_names(df)

    df = shorten_faculties(df)

    summary_dfs = get_counts(df)

    summary_dfs = clean_software_funding(summary_dfs)

    summary_dfs = change_lows_to_other(summary_dfs)

    find_number_responses(summary_dfs, df)

    # Prepare data for later graphing

    summary_dfs = sort_and_save(summary_dfs)

    summary_dfs = yes_and_no(summary_dfs)

    summary_dfs = scale_question_analysis(summary_dfs)

    summary_dfs = scale_worded_questions(summary_dfs)

    write_out_summaries(summary_dfs)

    # Conduct bivariate analysis
    bivariate_analysis(df, summary_dfs)

if __name__ == '__main__':
    main()
