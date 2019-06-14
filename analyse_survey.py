#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import numpy as np
import math


def import_csv_to_df(location, filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(location + filename + '.csv')


def export_to_csv(df, location, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(location + filename + '.csv', index=index_write)


def main():
    """
    Main function to run program
    """



if __name__ == '__main__':
    main()
