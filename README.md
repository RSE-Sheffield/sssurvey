# Survey of software use at the University of Sheffield

This is a fork of the original scripts used to generate the results of the Survey form the University of Southhampton publisged with the DOI: 10.5281/zenodo.3569549

In Novemeber 2020 the university of Sheffield conducted a survey of software use across all academic and researchstaff and PhD students. The survey was open for two weeks and collected 382 responses.

The raw data was cleaned to remove email addresses, for privacy reasons. The result of this cleaning is the file `data/sheffield.csv`.

## Results

A link to published results will be added to the readme in this location.

## Important points

* Licence for the code, data, reports and charts can be found in the the LICENCE, DATA LICENCE and REPORT LICENCE files respectively.
* The code runs on Python 3.

## Running the analysis

1. Get the files and data: [Clone the git repository](https://help.github.com/articles/cloning-a-repository/)
1. We suggest the use of a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/). The file `requirements.txt` can be used to load the necessary libraries.
1. Run the analysis script `analyse_survey.py`.

Note that the file `column_name_renaming.py` contains instructions for shortening the column names (using the full question for the column name gets tedious) and lists which questions are sorted in which way (some questions are best suited to the results being sorted by the size of response, others - like the scale questions that rank responses from 1 to 5 - require the results to be sorted in specific order (i.e. 1 to 5).

Bivariate analysis is controlled by the file `bivariate_instructions.py`. It's a dictionary called `which_by_which`. The values represent questions of interest and the key represents the question by which you wish to segment the questions of interest. For example, if you want to investigate how the number of people who develop code varies by faculty, you would set up the dictionary found in the `bivariate_instructions.py` file as follows:

`which_by_which = {'faculty': ['develop_own_code']}`

if you also wanted to investigate how the training question segemented by faculty, you would use a dictionary:

`which_by_which = {'faculty': ['develop_own_code', 'training']}`

The separate bivariate files (found in ```output_csv/bivariate```) are brought together into summary csvs by the script ```combine_bivariate_results_for_graphing.py``` to produce csvs the csvs found in ```output_csv/bivariate/summaries```

## Files and directories

* ```analyse_survey.py```: the main analysis script that converts the survey data into csvs that each summarise a question.
* ```column_name_renaming.py```: lookup file used for shortening names of columns of data.
* ```bivariate_instructions.py```: lookup file used to instruct ```analyse_survey.py``` on which bivariate analyses to conduct.
* ```combine_bivariate_results_for_graphing.py```: combines the individual bivariate csv files to produce useful summaries.
* ```UniSotonSoftwareSurvey_June2019.pdf```: a pdf file of the original survey used to collect the data
* ```data/Cleaning-of-Uni-Soton-Software-Survey-26Jun19.csv```: an anonymised version of the survey results
* ```output/csv/```: all output csvs are stored in this directory and the enclosed directories.
* ```report/Results of University of Southampton software survey June 2019.ipynb```: Jupyter notebook used to write report
* ```report/Results of University of Southampton software survey June 2019.pdf```: pdf of Jupyter notebook
* ```charts/```: charts of all the output csvs as png images
* ```charts/plot_details/```: csvs holding parameters used to draw charts

## Plotting

[Simon Hettricks plotting scripts](https://github.com/SimonHettrick/graphing) have been added to this repository to allow plotting. You can generate the plots by navigating to the graphiing directory and running ```python graphing.py ```.
