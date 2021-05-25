# My fancy-pants graphing program

## Summary

I'm tired of never getting the kind of charts I want out of Matplotlib. It\'s so damned fiddly. I put this together to do plotting in a way that I need for presentations, reports and things. At the moment, it works on a set of csvs, but it could easily be copied into existing code.

## What's what?

There are three directories: data, output and plot details.

* ```archived_plot_data```: a dir in which plot-detail-and-data archives are stored (see ```archive_plot_details.py```).
* ```archive_plot_details.py```: run this script after you've finished tailoring your plots if you want to zip up the plot-detail-and-data files into a handy, dated archive file. 
* ```chart_details_lookup.py```: holds global parameters that affect all plots: image size, resolution, etc.
* ```data```: holds a set of csv files that contain the data you want plotted.
* ```graphing.py``` is the script that produces the charts based on the details in the lookup table. If you want to reproduce all the charts regardless of whether they were previously created, use the command ```graphing.py ignore```.
* ```output```: holds the charts as a set of pngs
* ```plot_details```: uses ```default.csv``` to create a set of csvs - one for each file in the ```data``` dir - to tailor the plots. The parameters can be changed manually after the files are created to tailor the charts you want. 
* ```plot_details/previous_run```: this contains the version of the plot details csv files used in the last run. In the current run, ```graphing.py``` will check the current version of the plot details against the previous version and (to save everyone's time) will only recreate the chart if something has changed (unless you use the ```ignore``` argument (see above).
* ```requirements.txt``` holds the details of the libraries used by the scripts

## Set up

### Prepare for running Python:

Prepare for running Python:
1. If not already installed, [install virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
   * ```pip install virtualenv```
1. Create a project folder:
   * ```virtualenv -p <location of Python3 install directory> <name of project>```
1. Activate the virtual environment:
   * ```source <name of project>/bin/activate ```
1. Install libraries:
   * ```pip install -r requirements.txt ```
1. (If you're having lots of problems with pip not finding the right libraries, try [installing pip from source](https://pip.pypa.io/en/stable/installing/).)

### Set up the lookup file
 
1. Set parameters in ```global_specs``` within  ```chart_details_lookup.py``` to specify the size of the charts, the resolution of the saved charts, and the font used in the charts.

### Creating the details for each plot

* When you first run ```graphing.py``` it will take create plot details files for each csv it finds in the ```data``` directory. These will be based on the values in the ```default.csv``` file.
* So... if you have a favoured idea on the size of the title font or anything like that, change it in the ```default.csv``` file before running ```graphing.py``` for the first time. (If you have already completed that first run, just delete all the csvs from the ```data``` directory, make the change you wanted in the ```default.csv``` file and run ```graphing.py``` again.)
* You'll notice two fields (filename and chart_title) that exist in the generated csvs but not in the ```default.csv```. These parameters are created automatically by ```graphing.py```.
* The plotting parameters in each csv are:
   * filename: foo.csv -  the name of the csv in the data directory, generated automatically
   * plot_type: bar - the type of chart, currently bar charts are the only choice
   * y1_axis': 'percentage' - Name of the column you want plotted
   * y2_axis: False - Name of a second column you want plotted (or False, if there isn't one)
   * x_title: False - A title for the x-axis, or False if you don't want a title
   * x_rot: 0 - Rotation of x-axis tick labels (0 is horizontal)
   * x_max_len: 15 - Max length of x-axis tick labels before they start a new line
   * y_title: Percentage - Title for y axis, or use False if you don't want a title
   * chart_title: This is a title - Chart title, or use False if you don't want a title
   * show_values: True - If True, show value on bars, if False, nothing
   * symbol_after_value: % - Any symbol you add here will display after the relevant value if you choose ```show_values=True```. Most common use is to add a % symbol. Put ```False``` if you don't want any symbol to appear         
   * skip_labels: False - If False, print all x-axis labels. If set to a number, print an x-tick label, then skip that number of    * labels before printing the next x-axis label. (Allows you to deal with having too many x-tick labels to show neatly).
   * bottom_size: 0.15 - Fraction of chart dedicated to x-axis tick labels (must be in range 0 - 1)
   * title_font_size: 24 - Size of title font
   * axis_font_size: 14 - Size of axis fonts
   * value_font_size: 20 - Size of value label font
             
### Create charts

1. Set any default values that you like in the ```default.csv``` file and save it.
1. Copy your data csvs to the ```data``` directory
1. Assuming that your csvs are of the form:

| questions       | number | percentage |
|-----------------|--------|------------|
|Name             | 5      | 3          |
|Favourite colour | 4      | 2          |
|Swallow speed    | 2      | 1          |
|Question         | 1      | 1          |

1. At the start of the ```main``` function in ```graphing.py``` you will find a variable ```col_for_plot_data```. This should be set to the name of the column in which you list your questions (in the above example: ```col_for_plot_data = 'questions' ```.
1. Run ```graphing.py```
1. You will now have a populated ```plot_details``` directory and a series of charts in the ```output``` directory
1. Look through the charts, decide what changes you would like to make to the plotting parameters (listed above), make those changes and run ```graphing.py``` again.
1. Repeat the last step until you are satisfied with the results.
1. When you are finished tailoring your charts, you can run ```archive_plot_details.py``` to save the data csvs and your plot details for posterity. The resulting zip file can be found in ```archived_plot_data```. 


### Notes

1. If you want to see the charts as they are created, open ```python graphing.py``` and uncomment the following line:
 * ```#    plt.show()```
 * Note: you will now have to close each chart after it's opened by the script
