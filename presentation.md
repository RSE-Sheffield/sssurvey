% University of Sheffield Research Software Survey (2020) - WORK IN PROGRESS
% Robert Turner, Paul Richmond, University of Sheffield RSE Team
% September, 2021

# Sources

* Data and analysis software <https://github.com/RSE-Sheffield/sssurvey>.
* Report in `.pdf` format <https://github.com/RSE-Sheffield/sssurvey/blob/main/report.pdf>.

# Major Findings

::: incremental

* 382 respondents.
* 91% of respondents use research software ([92% nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).
* 65% report that software is vital to their research (nationally, 69% report that "It would not be practical to conduct my work without software").
* 27% develop their own code ([56% nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).
* 69% (of the 27% subset who responded to this question) feel they have **not had sufficient training** to develop reliable software.
* Of the 54% of respondents who are involved with writing funding proposals, 45% expected to write software as part of the proposal.
* Of those who expected to write software, 40% did not request funding for this (compared to [20%, nationally](https://zenodo.org/record/1183562#.YMnQFahKiUk)).

:::

# Recommendations

::: incremental

* Investigate why 69% of respondents feel they have not had sufficient training.
* Provide training / support to increase researcher confidence with version control, continuous integration and unit testing.
* Investigate why participants responded as they did to a question about level of support for software development. Create a target for this and monitor performance against it.
* Provide additional support to researchers to make research software outputs not intended for commercialisation freely available.
* Discover if any action can be taken to help researchers who would like to use University of Sheffield HPC but don't currently use to do so.
* Advocate for researchers to include costs for software development in their funding applications.

:::

# Sample characteristics

This survey and those we make comparisons with used different sampling strategies:

::: incremental

* This survey went to all PhD students and research staff with a prize incentive.
* A 2020 Southampton survey went to *"all staff employed on an ERE contract (Education, Research and Enterprise) and all PhD students"* with a prize incentive. As surveys were sent out on a faculty by faculty basis, it was possible to report a response rate of between 8% and 11% for all faculties.
* 2014 national survey - it is not clear what sampling strategy was used.

:::

# Sample Characteristics - Faculty

![In which faculty are you based?](charts/01_faculty.png)

# Sample Characteristics - Funders

![Which of the following organisations usually fund your research?](charts/02_funders.png)

# Sample Characteristics - Job

![What is your job title?](charts/03_job.png)

# Prevalence and importance of research software

:::::::::::::: {.columns}
::: {.column width="50%"}
![Do you use research software?](charts/04_use.png)
:::
::: {.column width="50%"}
![How important is research software to your work?](charts/05_important.png)

1 *"Not at all"*, to 5 *"Vital"*
:::
::::::::::::::

# Software development practise

:::::::::::::: {.columns}
::: {.column width="50%"}
![Have you developed your own research software?](charts/06_developed.png)
---
![Do you feel that you have received sufficient training to develop reliable software?](charts/08_training_exclude_no_response.png)
:::
::: {.column width="50%"}
![How do you rate your software development expertise?](charts/07_rate_dev_exclude_no_response.png)

1 *"Beginner"* to 5, *"Professional"*
:::
::::::::::::::

# Awareness around key skills

:::::::::::::: {.columns}
::: {.column width="50%"}
![Version control](charts/12_tech_vc_exclude_no_response.png)

![Continuous integration](charts/13_tech_ci_exclude_no_response.png)
:::
::: {.column width="50%"}
![Unit testing](charts/14_tech_test_exclude_no_response.png)
:::
::::::::::::::

# Current level of support

![How would you rate the university's current level of support for your software-development needs?](charts/15_support_exclude_no_response.png)

1: *"poor"* to 5: *"excellent"*

