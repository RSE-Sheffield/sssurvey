# University of Sheffield Research Software Survey 2020 Results

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RSE-Sheffield/sssurvey.git/HEAD?filepath=sheffield_software_report.ipynb)

Make HTML:

```
jupyter nbconvert --to html charts.ipynb --output ./docs/index.html --no-input 
```

## `data/`

### `raw/`

Anonymised data
### `clean/`

Data cleaned using (`01_clean_data.py`)[scripts/01_clean_data.py].

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
> git clone https://github.com/RSE-Sheffield/sssurvey.git
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
> python code/01_clean_data.py
> python code/02_plot.py
> ```

## `requirements.txt`

This file must list the package requirements needed to execute the code in `code/`.

Substitute `environment.yml` for `requirements.txt`, if appropriate. If using Jupyter notebooks, instructions may be better embedded within the notebook file.
