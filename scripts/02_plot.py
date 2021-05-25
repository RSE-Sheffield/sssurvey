import pandas as pd

from plotnine import * # Not generally good practise

sheffield_df = pd.read_csv('./data/clean/sheffield_clean.csv')

# Response by faculty
(ggplot(sheffield_df, aes(x='faculty')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/01_faculty_plot.png')

# Software use
(ggplot(sheffield_df, aes(x='use_software')) + 
    geom_bar() + 
    coord_flip()
).save('./plots/04_use_software.png')