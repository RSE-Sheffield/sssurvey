# University of Sheffield Research Software Survey 2020 Results

It consists of the following folders and files:

## `data/`

### `raw/`

Anonymised data
### `clean/`

Data cleaned using (`01_clean_data.py`)[scripts/01_clean_data.py].

## `notebooks/`

**Optional**

- Must contain Jupyer notebooks.
- There must (at a minimum) be clear seperation of function between data download, data munging and analysis. In the case of Jupyter notebooks these may be seperate headings, for scripts they may be seperate files.

## `scripts/`

Scripts used in data cleaning and analysis

## LICENSE

**Mandatory**

- If this folder is not in a repository which already has a license, an appropriate license is essential.

## `readme.md`

**Mandatory**

- Instructions to run the code, for example:

> Clone this repository:
> ```
> git clone https://github.com/airqo-platform/AirQo-experiments.git
> ```
> Change directory to this folder:
> ```
> cd reproducibility-template
> ```
> Create and activate clean conda enviroment:
> ```
> conda create --force -n reproducibility-template python=3.6
> conda activate reproducibility-template
> ```
> Install requirements:
> ```
> pip install -r requirements.txt
> ```
> Execute code:
> ```
> python code/01_get_data.py
> python code/02_clean_data.py
> python code/03_analysis.py
> ```

## `requirements.txt`

This file must list the package requirements needed to execute the code in `code/`.

Substitute `environment.yml` for `requirements.txt`, if appropriate. If using Jupyter notebooks, instructions may be better embedded within the notebook file.
