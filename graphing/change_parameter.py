#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import numpy as np
import os
import glob


PLOTDETAILSSTORE = './plot_details/'


def import_csv_to_df(filename, index_col):
    """
    Imports a csv file into a Pandas dataframe
    :params: get an xls file and a sheetname from that file
    :return: a df
    """

    return pd.read_csv(filename, index_col=index_col)


def export_to_csv(df, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(filename, index=index_write)


def get_graph_data():
    """
    Gets all the csv files in the data dir
    :return: a list of the dir path, filename and file extension for the csvs in the data dir
    """

    graph_datafiles = glob.glob(PLOTDETAILSSTORE + '/*.csv')

    return graph_datafiles

def change_parameter(graph_datafiles, parameter_to_change, new_value_for_parameter, colname_holding_values):

    for current_csv in graph_datafiles:
        filename = os.path.basename(current_csv)
        df = import_csv_to_df(PLOTDETAILSSTORE + filename, 'field')
        df.at[parameter_to_change, colname_holding_values] = new_value_for_parameter
        export_to_csv(df, PLOTDETAILSSTORE + filename, True)
    return

def main():
    """
    Main function to run program

    Choose a parameter to change from:

    filename: foo.csv - the name of the csv in the data directory, generated automatically
    plot_type: bar - the type of chart, currently bar charts are the only choice
    y1_axis': 'percentage' - Name of the column you want plotted
    y2_axis: False - Name of a second column you want plotted (or False, if there isn't one)
    x_title: False - A title for the x-axis, or False if you don't want a title
    x_rot: 0 - Rotation of x-axis tick labels (0 is horizontal)
    x_max_len: 15 - Max length of x-axis tick labels before they start a new line
    y_title: Percentage - Title for y axis, or use False if you don't want a title
    chart_title: This is a title - Chart title, or use False if you don't want a title
    show_values: True - If True, show value on bars, if False, nothing
    symbol_after_value: % - Any symbol you add here will display after the relevant value if you choose show_values=True. Most common use is to add a % symbol. Put False if you don't want any symbol to appear
    skip_labels: False - If False, print all x-axis labels. If set to a number, print an x-tick label, then skip that number of * labels before printing the next x-axis label. (Allows you to deal with having too many x-tick labels to show neatly).
    bottom_size: 0.15 - Fraction of chart dedicated to x-axis tick labels (must be in range 0 - 1)
    title_font_size: 24 - Size of title font
    axis_font_size: 14 - Size of axis fonts
    value_font_size: 20 - Size of value label font
    """

    parameter_to_change = 'axis_font_size'
    new_value_for_parameter = '6'
    colname_holding_values = 'value'

    graph_datafiles = get_graph_data()

    change_parameter(graph_datafiles, parameter_to_change, new_value_for_parameter, colname_holding_values)

if __name__ == '__main__':
    main()