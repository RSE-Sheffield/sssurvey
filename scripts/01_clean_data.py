# Code used to clean and combine data into a form in which it can be analysed.
import pandas as pd

# Get details for plots from look up table
from column_name_renaming import col_shortener

wip_df = pd.read_csv('./data/raw/sheffield.csv')

# Rename columns
wip_df.rename(index=str, columns=col_shortener, inplace=True)

# Drop timestamp
wip_df.drop(labels=['Timestamp'], axis='columns', inplace=True)

# Shorten faculty names
wip_df['faculty'].replace(regex=True, inplace=True, to_replace=r'Faculty of ', value=r'')

# Shorten wordy answers
wip_df['ready_to_share'].replace(inplace=True, to_replace='I\'m not interested in commercialising my research software', value='Not interested')

wip_df['ready_to_share'].replace(inplace=True, to_replace='No (I\'m not involved in writing funding proposals)', value='No, no proposals')
wip_df['ready_to_share'].replace(inplace=True, to_replace='No (but we DID expect to write software as part of the project)', value='No, software development expected')
wip_df['ready_to_share'].replace(inplace=True, to_replace='No (we did NOT expect to write software as part of the project)', value='No, software development not expected')

# Change types
wip_df['faculty'] = wip_df['faculty'].astype('category')
wip_df['funders'] = wip_df['funders'].astype('string') # Multi select and other
wip_df['job_title'] = wip_df['job_title'].astype('string')
wip_df['use_software'] = wip_df['use_software'].astype('category') # Yes / No
wip_df['importance_software'] = wip_df['importance_software'].astype('category')
wip_df['develop_own_code'] = wip_df['develop_own_code'].astype('category') # Yes / No
wip_df['development_expertise'] = wip_df['development_expertise'].astype('category')
wip_df['training'] = wip_df['training'].astype('category') # Yes / No
wip_df['want_to_commercialise'] = wip_df['want_to_commercialise'].astype('category') # Yes / No
wip_df['ready_to_share'] = wip_df['ready_to_share'].astype('category') # Yes / No / Other
wip_df['hpc_use'] = wip_df['hpc_use'].astype('category')
wip_df['version_control'] = wip_df['version_control'].astype('category')
wip_df['continuous_integration'] = wip_df['continuous_integration'].astype('category')
wip_df['unit_testing'] = wip_df['unit_testing'].astype('category')
wip_df['current_support'] = wip_df['current_support'].astype('category')
wip_df['hired_developer'] = wip_df['hired_developer'].astype('category') # Yes / No
wip_df['funds_for_development'] = wip_df['funds_for_development'].astype('string') # Multi select and other
wip_df['hire_full_time_developer'] = wip_df['hire_full_time_developer'].astype('category')
wip_df['hire_rse'] = wip_df['hire_rse'].astype('category')

# Save clean data
wip_df.to_csv('./data/clean/sheffield_clean.csv', index=False)