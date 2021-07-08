import pandas as pd
from pandas.core.algorithms import unique

# Get details for plots from look up table
from column_name_renaming import col_shortener

wip_df = pd.read_csv('./data/raw/sheffield.csv')

# Deal with nulls
wip_df.fillna('No response', inplace=True)

# Rename columns
wip_df.rename(index=str, columns=col_shortener, inplace=True)

# Get unique self described job titles
unique_jobs = wip_df['job_title'].unique()
pd.DataFrame.from_dict({'raw_job' : unique_jobs, 'clean_job' : [None] * unique_jobs.size}).to_csv('./data/working/unique_job_list.csv', index=False)

# Make and save list of funders
funders_sos = wip_df['funders'].str.split(pat=r'[,;]')
funders = funders_sos.apply(pd.Series).stack().reset_index(drop = True)
funder_df = pd.DataFrame({'funder' : funders})
funder_df['funder'] = funder_df['funder'].str.strip()
funder_df.to_csv('./data/working/funders.csv', index=False)

# Get unique self-descibed funding sources
unique_funders = funder_df['funder'].unique()
pd.DataFrame.from_dict({'raw_funders' : unique_funders, 'clean_funders' : [None] * unique_funders.size}).to_csv('./data/working/unique_funders_list.csv', index=False)