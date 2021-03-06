# Code used to clean and combine data into a form in which it can be analysed.
import pandas as pd

# Get details for plots from look up table
from column_name_renaming import col_shortener

# Load raw data
wip_df = pd.read_csv('./data/raw/sheffield.csv')

# Deal with nulls
wip_df.fillna('No response', inplace=True)

# Rename columns
wip_df.rename(index=str, columns=col_shortener, inplace=True)

# Drop timestamp
wip_df.drop(labels=['Timestamp'], axis='columns', inplace=True)

# Shorten faculty names
wip_df['faculty'].replace(regex=True, inplace=True, to_replace=r'Faculty of ', value=r'')

# Tidy job titles
unique_job_list_mapped_df = pd.read_csv('./data/working/unique_job_list_mapped.csv') # This mapping was produced semi-manually
wip_df = wip_df.merge(unique_job_list_mapped_df, left_on='job_title', right_on='raw_job', how='left')

# Shorten wordy answers
wip_df['ready_to_share'].replace(inplace=True, to_replace='I\'m not interested in commercialising my research software', value='Not interested')

wip_df['ready_to_share'].replace(inplace=True, to_replace='No (I\'m not involved in writing funding proposals)', value='No, no proposals')
wip_df['ready_to_share'].replace(inplace=True, to_replace='No (but we DID expect to write software as part of the project)', value='No, software development expected')
wip_df['ready_to_share'].replace(inplace=True, to_replace='No (we did NOT expect to write software as part of the project)', value='No, software development not expected')

# Save clean data
wip_df.to_csv('./data/clean/sheffield_clean.csv', index=False)

# Make and save list of funds for development responses
funds_for_development_sos = wip_df['funds_for_development'].str.split(pat=r'[,;]')
funds_for_development = funds_for_development_sos.apply(pd.Series).stack().reset_index(drop = True)
funds_for_development_df = pd.DataFrame({'funds_for_development' : funds_for_development})
funds_for_development_df['funds_for_development'] = funds_for_development_df['funds_for_development'].str.strip()
funds_for_development_df.to_csv('./data/clean/funds_for_development_clean.csv', index=False)

# Count job titles (facilitates plotting where there are many different job titles)
job_title_counts = wip_df['clean_job'].to_frame().groupby('clean_job').size().reset_index(name='counts')
job_title_counts.to_csv('./data/clean/job_title_counts_clean.csv', index=False)

# Tidy funders
funders_df = pd.read_csv('./data/working/funders.csv') 
unique_funders_list_mapped_df = pd.read_csv('./data/working/unique_funders_list_mapped.csv') # This mapping was produced semi-manually
funders_df = funders_df.merge(unique_funders_list_mapped_df, left_on='funder', right_on='raw_funders', how='left')
funders_df.to_csv('./data/clean/funders_clean.csv', index=False)

# Count funders (facilitates plotting where there are many different funders)
funder_counts = funders_df.groupby('clean_funders').size().reset_index(name='counts')
funder_counts.to_csv('./data/clean/funder_counts_clean.csv', index=False)