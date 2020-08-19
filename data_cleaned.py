#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:42:53 2020

@author: liuchen
"""

import pandas as pd
df = pd.read_csv('Marketing Specialist.csv')

#drop unuseful columns
df2 = df.drop(['Headquarters'], inplace = True, axis = 1)
df1 = df.drop(['Competitors'], inplace = True,axis = 1)

#cleaning irrelevant information in salary column 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
cleaned_salary = salary.apply(lambda x: x.replace('$','').replace('K',''))

#finding out minmun salary & max salary & average salary
df['min_salary'] = cleaned_salary.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = cleaned_salary.apply(lambda x: int(x.split('-')[1]))
df['average_salary'] = (df['min_salary'] + df['max_salary'])/2

# transforme '-1' rating into '1'
df['rating_cleaned'] = df['Rating'].apply(lambda x: 1 if x == -1 else x)

#make company name cleaner
df['company_name_cleaned'] = df.apply(lambda x: x['Company Name'] if x['Rating'] == -1 else x['Company Name'][:-3], axis = 1)

#get state
df['state'] = df['Location'].apply(lambda x: x.split(',')[-1])

df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'alabama' else 'AL')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'united states' else 'Remote')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'massachusetts' else 'MA')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'illinois' else 'IL')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip() != 'New Jersey' else 'NJ')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'kansas' else 'IL')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'california' else 'CA')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'virginia' else 'VA')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'ohio' else 'OH')
df['state'] = df['state'].apply(lambda x: x.strip() if x.strip().lower() != 'pennsylvania' else 'PA')

# transforme '-1' [size] into 'Unknown'
df['size cleaned'] = df['Size'].apply(lambda x: 'Unknown' if x == '-1' else x)

# calculate company's age
df['age'] = df['Founded'].apply(lambda x: 'Unknown' if x == -1 else 2020 - x)

#clean [ownership]
df['ownership_cleaned'] = df['Type of ownership'].apply(lambda x: 'Unknown' if x == '-1' else x)
df['ownership_cleaned'] = df['ownership_cleaned'].apply(lambda x: x.strip() if x.strip().lower() != 'other organization' else 'Unknown')
df['ownership_cleaned'] = df['ownership_cleaned'].apply(lambda x: x.strip() if x.strip().lower() != 'school / school district' else 'College / University')
df['ownership_cleaned'] = df['ownership_cleaned'].apply(lambda x: x.strip() if x.strip().lower() != 'private practice / firm' else 'Company - Private')

#transforme '-1' [industry] into 'others'
df['Industry_cleaned'] = df['Industry'].apply(lambda x: 'others' if x == '-1' else x)

#transforme '-1' [sector] into 'others'
df['sector_cleaned'] = df['Sector'].apply(lambda x: 'others' if x == '-1' else x)

#clean [revenue]
df['revenue_cleaned'] = df['Revenue'].apply(lambda x: x.split('/')[0])
df['revenue_cleaned'] = df['revenue_cleaned'].apply(lambda x: 'Unknown' if x == '-1' else x)

df_out = df
df_out.to_csv('data_cleaned.csv',index = False)
