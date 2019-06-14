#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
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


def rename_cols(df):

    return df.rename(index=str, columns=col_shortener)

def get_counts(df, grouped_cols):

    # Storing results as a dict of dfs
    univariate_summary_dfs = {}



def main():
    """
    Main function to run program
    """

    df = import_csv_to_df(DATAFILELOC, DATAFILENAME)

    df = rename_cols(df)

    print(df)

    # get_counts(df,)


if __name__ == '__main__':
    main()
