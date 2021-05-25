#!/usr/bin/env python
# encoding: utf-8

import glob
import os
from zipfile import ZipFile
from datetime import date


DATASTORE = './data/'
PLOTDETAILSSTORE = './plot_details/'
ARCHIVESTORE = './archived_plot_data/'
CHARTSTORE = './output/'

def get_file_names(directory):
    """
    Get the names of the completed csv files used to store the plot details
    """

    return glob.glob(directory + '/*.csv')

def get_other_filenames(filenames):

    datafilenames = []

    for list_item in filenames:
        basename = os.path.splitext(os.path.basename(list_item))[0]
        # Get the data csvs
        datafilenames.append(DATASTORE + basename + '.csv')
        # Get the chart pngs
        datafilenames.append(CHARTSTORE + basename + '.png')

    return datafilenames



def get_date():

    return date.today()


def get_zipname(date):

    """
    Finds out what I want the zipfile called. Adds the date so that I can track these things
    and replaces spaces with underscores because I am one inconsistent mofo.
    :param date: today's date
    :return: a nicely formatted filename for the zip file
    """

    while True:
        zipname = input('What do you want to call the zip file? ')
        zipname = zipname.replace(' ', '_')
        zipname = str(date) + '_' + str(zipname) + '.zip'
        print('The zipfile will be called "' + zipname + '"')
        proceed = input ('Happy to proceed? (y/n) ')
        if proceed.lower() == 'y':
            break

    return zipname


def zipfiles(filenames, datafilenames, zipname):

    all_filenames = filenames + datafilenames

    # create a ZipFile object
    zip_obj = ZipFile(ARCHIVESTORE + zipname, 'w')

    for list_item in all_filenames:
        zip_obj.write(list_item)

    # close the Zip File
    zip_obj.close()

    return

def main():
    """
    Main function to run program
    """
    # Whereas I might have left old data files in the data dir, the plot details dir
    # will always have the most up to date version of what I
    # was doing (because they dictate what gets plotted so you get tons of extraneous plots
    # if you're not good with your folder discipline in this dir.
    # Hence start with the files in the plot dir and use that to identify the data csvs and plot pngs

    filenames = get_file_names(PLOTDETAILSSTORE)

    # Get the data and charts that corresponds to the plot details
    datafilenames = get_other_filenames(filenames)

    print(datafilenames)

    date = get_date()

    # User input for zip filename
    zipname = get_zipname(date)

    zipfiles(filenames, datafilenames, zipname)

if __name__ == '__main__':
    main()