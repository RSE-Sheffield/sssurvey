import altair as alt
import pandas as pd

from plotnine import * # Not generally good practise

sheffield_df = pd.read_csv('./data/clean/sheffield_clean.csv')

funders_df = pd.read_csv('./data/clean/funders_clean.csv')

# Response by faculty
(ggplot(sheffield_df, aes(x='faculty')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/01_faculty_plot.png')

alt.Chart(sheffield_df).mark_bar().encode(
    alt.Y('faculty:N'),
    alt.X('count(faculty):Q')
).save('./plots/01_faculty_plot_alt.html')

# Funders
(ggplot(funders_df, aes(x='funder')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/02_funders.png')

# Job titles
(ggplot(sheffield_df, aes(x='clean_job')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/03_clean_job.png')

# Software use
(ggplot(sheffield_df, aes(x='use_software')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/04_use_software.png')

# Software importance
(ggplot(sheffield_df, aes(x='importance_software')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/05_importance_software.png')

# Develop code
(ggplot(sheffield_df, aes(x='develop_own_code')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/06_develop_own_code.png')

# Expertise self assesment
(ggplot(sheffield_df, aes(x='development_expertise')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/07_development_expertise.png')

# Enough training
(ggplot(sheffield_df, aes(x='training')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/08_training.png')

# Want to commercialise
(ggplot(sheffield_df, aes(x='want_to_commercialise')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/09_want_to_commercialise.png')

# Ready to commercialise
(ggplot(sheffield_df, aes(x='ready_to_share')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/10_ready_to_share.png')

# HPC use
(ggplot(sheffield_df, aes(x='hpc_use')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/11_hpc_use.png')

# Version control
(ggplot(sheffield_df, aes(x='version_control')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/12_version_control.png')

# CI
(ggplot(sheffield_df, aes(x='continuous_integration')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/13_continuous_integration.png')

# Unit testing
(ggplot(sheffield_df, aes(x='unit_testing')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/14_unit_testing.png')

# Current support OK?
(ggplot(sheffield_df, aes(x='current_support')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/15_current_support.png')

# Hired developer?
(ggplot(sheffield_df, aes(x='hired_developer')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/16_hired_developer.png')

# Asked for funds
(ggplot(sheffield_df, aes(x='funds_for_development')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/17_funds_for_development.png')

# Want full time developer
(ggplot(sheffield_df, aes(x='hire_full_time_developer')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/18_hire_full_time_developer.png')

# Want RSE
(ggplot(sheffield_df, aes(x='hire_rse')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/19_hire_rse.png')