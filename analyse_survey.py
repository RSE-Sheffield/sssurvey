#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import matplotlib
# You have to use this library to sidestep a problem with Python not being installed as a framework
# on a Mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import math


# Get details for plots from look up table
from column_name_renaming import col_shortener


DATAFILELOC = "./data/"
DATAFILENAME = "UniSotonSoftwareSurvey-csv.csv"
STOREFILENAME = "./output/"


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


def clean_col_names(df):
    """
    Takes a dict from a look up file and uses it to rename the columns
    to something shorter and tidier
    :param df: the main df
    :return: the main df with new col names
    """


    return df.rename(index=str, columns=col_shortener)

def get_counts(df):
    """
    Conduct univariate analysis
    :param df: the main df
    :return: a dict of dfs that contain the results
    """

    # Initiailise a dict into which I shall store the results dfs
    univariate_summary_dfs = {}

    # Go through each col, get the counts of each question, calculate a percentage and then store as a result df
    for current_col in df.columns:
        df_counts = pd.DataFrame(data = (df[current_col].value_counts(sort=False)), columns = [current_col])
        df_counts['percentage'] = round(100 * df_counts[current_col] / df_counts[current_col].sum(), 0)
        univariate_summary_dfs[current_col] = df_counts



    return univariate_summary_dfs



def main():
    """
    Main function to run program
    """

    df = import_csv_to_df(DATAFILELOC, DATAFILENAME)

    df = clean_col_names(df)


    get_counts(df)


if __name__ == '__main__':
    main()
