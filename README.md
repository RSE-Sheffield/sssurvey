### Survey of software use at the University of Southampton

In June 2019 we conducted a survey of software use across 6355 academic staff and PhD students. The survey was open for two weeks and collected 603 responses.

The raw data was cleaned using Open Refine to remove email addresses for privacy reasons, to remove responses that were not valid (namely responses that were not associated with a known faculty at the University of Southampton) and to reduce the job title provided by the respondents into a set of known job titles (e.g. convert "Prof", "Professor", "Proffessor" [sic] to "Professor"). The result of this cleaning is the file `data/Cleaning-of-Uni-Soton-Software-Survey-26Jun19.csv`.

## Important points

* Licence for the code and data can be found in the the LICENCE and DATA LICENCE files respectively.
* The code runs on Python 3.

## Running the analysis


1. Get the files and data: [Clone the git repository](https://help.github.com/articles/cloning-a-repository/)
1. We suggest the use of a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/). The file `requirements.txt` can be used to load the necessary libraries.
1. Run the analysis script `analyse_survey.py`.

Note that the file `column_name_renaming.py` contains instructions for shortening the column names (using the full question for the column name gets tedious) and lists which questions are sorted in which way (some questions are best suited to their answers being sorted by the size of response, others - like the scale questions that rank responses from 1 to 5 - require the answers to be sorted in specific order (i.e. 1 to 5).

Bivariate analysis is controlled by the file `bivariate_instructions.py`. It's a dictionary called `which_by_which`. The values represent questions of interest and the key represents the question by which you wish to segment the questions of interest. For example, if you want to investigate how the number of people who develop code varies by faculty, you would use a dictionary:

`which_by_which = {'faculty': ['develop_own_code']}`

and if you also wanted to investigate how the training question segemented by faculty, you would use a dictionary:

`which_by_which = {'faculty': ['develop_own_code', 'training']}`

## Files

Univariate results are stored in the `output_csvs`.
