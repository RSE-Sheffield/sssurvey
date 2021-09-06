# University of Sheffield Research Software Survey (2020)
<style>
    .reveal h1 { font-size: 2em; }
</style>

Robert Turner, Paul Richmond, University of Sheffield RSE Team
September, 2021

# Thank you!

Thanks for coming, thanks to the conference organisers, thanks to the RSE team at Sheffield, Paul Richmond in particular.

# About me

![Bob Turner](images/bobicorn.jpg){ height=256px }

Mix of software engineering and research experience.

# RSE at Sheffield

![RSE](https://github.com/RSE-Sheffield/RSE-Sheffield.github.io/raw/master/assets/images/logo/rse-logoonly-stroke.png){ height=256px }

13 RSEs, 35 projects / year worth ~£11m total

# Why survey?

::: incremental

* Improve our practise and procedures.
* Prioritise our resources.
* Data-driven advocacy.

:::

# I'm scared of surveys

![Ryanair](images/ryanair.jpg){ height=256px }

from *"The Art of Statistics: Learning from Data, David Spiegelhalter, 2020 paperback"*

# Reasoning

![Inductive inference](images/inference.svg)

from *"The Art of Statistics: Learning from Data, David Spiegelhalter, 2020 paperback"*

# Sources

* Data and analysis software <https://github.com/RSE-Sheffield/sssurvey>.
* Report in `.pdf` format <https://github.com/RSE-Sheffield/sssurvey/releases/download/latest/report.pdf>.

# The Survey

::: incremental

* Based on surveys carried out [nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk) in 2014 and at the [University of Southampton](https://zenodo.org/record/3569558#.YRZfS4hKiUl) in 2019, led by Simon Hettrick.
* Asked about "demographics", use and development of software, training and funding.

:::

# Analysis

*Generally, "non responses" to optional (O) questions were ignored. Mandatory questions are marked (M).*

::: incremental

* Data anonymised manually.
* Cleaned and annotated using Python scripts (with some manual decisions).
* Plotted charts using Jupyter notebook.
* Presentation and report written in markdown.
* Outputs built using pandoc / GitHub actions.

:::

# Sample characteristics

::: incremental

* This survey went to all PhD students and research staff with a prize incentive.
* 382 respondents.
* A 2019 Southampton survey went to *"all staff employed on an ERE contract (Education, Research and Enterprise) and all PhD students"* with a prize incentive. As surveys were sent out on a faculty by faculty basis, it was possible to report a response rate of between 8% and 11% for all faculties.
* 2014 national survey - it is not clear what sampling strategy was used.

:::

# Faculty

![In which faculty are you based? (M)](charts/01_faculty.png)

# Funders

![Which organisations usually fund your research? (O)](charts/02_funders.png)

# Job

![What is your job title? (O)](charts/03_job.png)

# Importance of research software

:::::::::::::: {.columns}
::: {.column width="50%"}
![Do you use research software? (M)](charts/04_use.png)
:::
::: {.column width="50%"}
![How important is research software to your work? (M)](charts/05_important.png)

1 *"Not at all"*, to 5 *"Vital"*
:::
::::::::::::::

# Software development practise

![Have you developed your own research software? (M)](charts/06_developed.png)

# Software Importance

::: incremental

* 91% of respondents use research software ([92% nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).
* 65% report that software is vital to their research (nationally, 69% report that "It would not be practical to conduct my work without software").
* 27% develop their own code ([56% nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).

:::

# Sufficiency of training

![Do you feel that you have received sufficient training to develop reliable software? (O)](charts/08_training_exclude_no_response.png)

# Awareness around key skills

:::::::::::::: {.columns}
::: {.column width="33%"}
![Version control (O)](charts/12_tech_vc_exclude_no_response.png)
:::
::: {.column width="33%"}
![Continuous integration (O)](charts/13_tech_ci_exclude_no_response.png)
:::
::: {.column width="33%"}
![Unit testing (O)](charts/14_tech_test_exclude_no_response.png)
:::
::::::::::::::

# Current level of support

![How would you rate the university's current level of support for your software-development needs? (O)](charts/15_support_exclude_no_response.png)

1: *"poor"* to 5: *"excellent"*

# Training and funding

::: incremental

* 69% (of the 27% subset who responded to this question) feel they have **not had sufficient training** to develop reliable software.
* Current level of support for software development is questionable.

:::

# Funding for Software Development

![Have you ever included costs for software development in a funding proposal? (excluding those who not involved in writing funding proposals) (M)](charts/17a_funding_excl_not_funding.png)

# Funding

::: incremental

* Of the 54% of respondents who are involved with writing funding proposals, 45% expected to write software as part of the proposal.
* Of those who expected to write software, 40% did not request funding for this (compared to [20%, nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).

:::

# Staffing of software development

:::::::::::::: {.columns}
::: {.column width="50%"}
![Hire a full-time software developer (M)](charts/18_model_ft_exclude_no_response.png)
:::
::: {.column width="50%"}
![Have you or someone in your group ever hired someone specifically to develop software? (M)](charts/16_hired.png)
:::
::::::::::::::

# Hiring practise

![Recruit a developer (or fractional FTE equivalent of a developer) from a central University of Sheffield pool as needed (O)](charts/19_model_rse_exclude_no_response.png)

# High Performance Computing

![Have you used ShARC/Bessemer, the University's high-performance computing (HPC) system? (M)](charts/11_hpc_exclude_no_response.png)

# Licensing and commercialisation

:::::::::::::: {.columns}
::: {.column width="50%"}
![Would you be interested in the university helping you commercialise some of your research software? (O)](charts/09_commercialise_exclude_no_response.png)
:::
::: {.column width="50%"}
![Do you feel that your research software is ready to be shared with a commercial partner? (M)](charts/10_partner_exclude_no_response.png)
:::
::::::::::::::

# Actions - training

::: incremental

* Provide training / support to increase researcher confidence with version control, continuous integration and unit testing.
* **Investigate why 69% of respondents feel they have not had sufficient training. What training is needed? How much?**

:::

# Actions

::: incremental

* Investigate why participants responded as they did to a question about level of support for software development.
* Provide additional support to researchers to make research software outputs not intended for commercialisation freely available.
* Discover if any action can be taken to help researchers who would like to use University of Sheffield HPC but don't currently use to do so.
* **Advocate for researchers to include costs for software development in their funding applications.**

:::

# Future work (Final Slide)

::: incremental

* Can we say if responses are different for different funders, research subjects using subgroup analysis?
* Does the national / international picture need to be revisited?

:::
