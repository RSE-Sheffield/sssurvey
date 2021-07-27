# University of Sheffield Research Software Survey 2020 Results

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RSE-Sheffield/sssurvey.git/HEAD?filepath=sheffield_software_report.ipynb)

## `data/`

### `raw/`

Anonymised data
### `clean/`

Data cleaned using (`01_clean_data.py`)[scripts/01_clean_data.py].

### `working/`

Intermediate data that required manual annotation during processing.

## `scripts/`

Scripts used in data cleaning and analysis

## LICENSE

The contents of this repository contributed by [@mondus](https://github.com/mondus) and [@bobturneruk](https://github.com/bobturneruk) are available under [this license](LICENSE). The contents of this repository contributed by [@SimonHettrick](https://github.com/SimonHettrick) are available under [this license](source_material/LICENSE).

# Installation

- Instructions to run the code, for example:

> Clone this repository:
> ```
> git clone https://github.com/RSE-Sheffield/sssurvey.git
> ```
> Change directory to this folder:
> ```
> cd sssurvey
> ```
> Create and activate clean conda enviroment:
> ```
> conda create --force -n sssurvey python=3.7
> conda activate sssurvey
> ```
> Install requirements:
> ```
> pip install -r requirements.txt
> ```

# Reproducing the analysis

## Data cleanup

> Execute code:
> ```
> python scripts/00_make_cleanup_helpers.py
> ```

This will regenerate files in `data/working`. A manual process is required to map the funders listed in `unique_funders_list.csv` and `unique_jobs_list.csv` to clean, consistent nomenclature (as these fields had free text options).

> Execute code:
> ```
> python scripts/01_clean_data.py
> ```

This will regenerate the contents of `data/clean`.

## Make charts

Load the notebook `charts.ipynb` and click "Restart and run all". This will regenerate the charts in `charts`.
