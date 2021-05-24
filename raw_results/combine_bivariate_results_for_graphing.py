#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import glob
import os

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


def get_files():
    """
    Gets a list of the csvs stored in teh bivariate folder
    :return: a list of these files
    """

    return glob.glob(BIVARIATESTORE + '/*.csv')


def get_dataframe(list_of_files):
    """
    Takes the list of bivariate csvs filenames and deconstructs them into
    a dataframe that can be used to grab the right files for merging the
    "blocks" of csvs together
    :param list_of_files: a list of the bivariate csvs
    :return: a df
    """

    blocks = []

    for current in list_of_files:
        filename = os.path.basename(os.path.splitext(current)[0])
        temp_list=filename.split("_sep_")
        temp_list.append(current)
        print(temp_list)
        blocks.append(temp_list)

    # First set is the question of interest and second set is the question that's used to segmen
    # the first set. For example, first set might be "Do you use software" and the second set
    # might be "what faculty are you in", and we want "who uses software by faculty"
    df_lists = pd.DataFrame(blocks, columns=['block', 'first_set', 'second_set', 'path'])
    # Don't need to sort it, but it makes it easier to check that things are going okay by eye
    df_lists.sort_values(by=['block', 'second_set'], inplace=True)

    return df_lists


def get_unique_blocks(df_lists):
    """
    Boils down the blocks col of df_lists to find the unique blocks
    :param df_lists:
    :return:
    """

    unique_blocks = list(df_lists['block'].unique())

    return unique_blocks


def get_bivariates(df_lists, unique_blocks):

    bivariates = {}

    for current_block in unique_blocks:
        temp_df = df_lists[df_lists['block']==current_block]
        unique_seconds = list(temp_df['second_set'].unique())
        bivariates[current_block] = (unique_seconds)

    return bivariates


def construct_bivariates_dfs(df_lists, unique_blocks, bivariates):
    """
    Get a dict of dfs that each include only the pertinent information needed to summarise
    each bivariate analysis
    :param df_lists: a df of all the bivariate analysis, the two questions included in it and the
            the paths back to the original csvs
    :param unique_blocks: a list of the unique blocks of bivariate analysis
    :param bivariates: a dict of each block of bivariate analysis and the unique second questions that take
            place within that block
    :return indiv_bivariate_dfs: a dict of dfs each one containing all the data needed to reconstruct a specific bivariate
            analysis
    """
    indiv_bivariate_dfs = {}

    for key in bivariates:
        temp_df = df_lists[df_lists['block']==key]
        for current_second in bivariates[key]:
            temp_df_2 = temp_df[temp_df['second_set']==current_second]
            indiv_bivariate_dfs[str(key) + '_' + current_second] = temp_df_2

    return indiv_bivariate_dfs


def reconstruct_single_bivariate_analyses(indiv_bivariate_dfs):

    bivariate_summaries = {}

    for current_df in indiv_bivariate_dfs:
        temp_df = indiv_bivariate_dfs[current_df]
        files_to_open = list(temp_df['path'])
        #print(current_df)

        dict_of_bivariates = {}
        for current_file in files_to_open:
            #print(current_file)
            new_row_name = current_file.split('_sep_')[1]
            # import_csv... takes a location and filename, rather than messing about splitting up the
            # path, I'll just submit the path as the location and submit a null for the filename. I know
            # it's a bit hacky, but not terrible.
            temp_df_2 = import_csv_to_df(current_file,'')
            temp_df_2.drop(columns='percentage', inplace=True)
            temp_df_2.set_index(['answers'], inplace=True)
            #print(temp_df_2)
            temp_df_2.columns = [new_row_name]
            #print(current_file)
            dict_of_bivariates[current_file] = temp_df_2

        final_summary_df = pd.concat(dict_of_bivariates.values(), sort=False, ignore_index=False, axis=1)
        final_summary_df = final_summary_df.transpose()

        export_to_csv(final_summary_df, BIVARIATESTORE + 'summaries/', 'summary_of_' + str(current_df), True)
        name_of_summary = current_df.split('_')

        print('here ' + current_df)
        print(final_summary_df)

    return




def main():
    """
    Main function to run program
    """

    list_of_files = get_files()

    df_lists = get_dataframe(list_of_files)

    unique_blocks = get_unique_blocks(df_lists)

    bivariates = get_bivariates(df_lists, unique_blocks)

    indiv_bivariate_dfs = construct_bivariates_dfs(df_lists, unique_blocks, bivariates)

    reconstruct_single_bivariate_analyses(indiv_bivariate_dfs)

if __name__ == '__main__':
    main()