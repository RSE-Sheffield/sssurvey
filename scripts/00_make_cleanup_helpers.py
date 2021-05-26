import pandas as pd
from pandas.core.algorithms import unique

# Get details for plots from look up table
from column_name_renaming import col_shortener

wip_df = pd.read_csv('./data/raw/sheffield.csv')

# Deal with nulls
wip_df.fillna('No response', inplace=True)

# Rename columns
wip_df.rename(index=str, columns=col_shortener, inplace=True)

# Get unqiue self described job titles
unique_jobs = wip_df['job_title'].unique()
pd.DataFrame.from_dict({'raw_job' : unique_jobs, 'clean_job' : [None] * unique_jobs.size}).to_csv('./data/working/unique_job_list.csv', index=False)