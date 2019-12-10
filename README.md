# Survey of software use at the University of Southampton

DOI: 10.5281/zenodo.3569549

In June 2019 we conducted a survey of software use across 6355 academic staff and PhD students. The survey was open for two weeks and collected 603 responses.

The raw data was cleaned using Open Refine to remove email addresses, for privacy reasons, to remove responses that were not valid (namely responses that were not associated with a known faculty at the University of Southampton) and to reduce the job title provided by the respondents into a set of known job titles (e.g. convert "Prof", "Professor", "Proffessor" [sic] to "Professor"). The result of this cleaning is the file `data/Cleaning-of-Uni-Soton-Software-Survey-26Jun19.csv`.

## Results

If you want quick access to the results, take a [look at the report](https://github.com/Southampton-RSG/soton_software_survey_analysis_2019/blob/master/report/Results%20of%20University%20of%20Southampton%20software%20survey%20June%202019.pdf).

Charts of the univariate analysis can also be seen in [this simple presentation](https://slides.com/simonhettrick/results-of-university-of-southampton-software-survey).

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

You can plot the csv files using any graphing program of your choice. Personally, I use a [graphing program I wrote in Python](https://github.com/SimonHettrick/graphing) to make the results look pretty. Feel free to use it too (made easier if you use the pre-existing parameters in the csvs held in ```report/charts/plot_details/```.
