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

def get_bivariates():
    """
    Gets all the csv files in the bivariates dir
    :return: a list of the dir path, filename and file extension for the csvs in the bivariate dir
    """

    dict_of_bivariates = {}

    list_of_bivariates = glob.glob(BIVARIATESTORE + '/*.csv')

    list_of_bivariates.sort()


    for current in list_of_bivariates:
        filename = os.path.basename(current)
        print(filename)
        #print(filename.split("_sep_")[0])


    return list_of_bivariates

def main():
    """
    Main function to run program
    """
    list_of_bivariates = get_bivariates()

if __name__ == '__main__':
    main()