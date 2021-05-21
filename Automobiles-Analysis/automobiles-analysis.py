#!/usr/bin/env python
# coding: utf-8

# # Project Goals
# 
# We have come across the data for various automobiles and will be performing a data analysis and correlation for various columns.<br>
# We first start by importing all the modules required for the analysis.

# In[2]:


import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import nbconvert


# <br>
# Next we load the data into a dataframe and see if it is valid enough to be analysed.
# <br>

# In[3]:


df = pd.read_csv('auto.csv')
display(df.head())


# <br>We observe that there seems to be no headers for the given data and we also have different values in the dataframe which have `?` as value which needs to be addressed.<br> We start by naming the headers/columns for the data.

# In[4]:


df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",              "num-of-cylinders", "engine-size","fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm",              "city-mpg", "highway-mpg", "price"]
df = df.replace('?',np.NaN)
display(df.head())


# <br>
# Now that we have replaced all the `?` in the data with a NaN value, now it is time to deal with the missing data in the datafraem. But before that, we need to find all the columns which have the missing values.

# In[5]:


null_col_list = []
for column in df.columns.values:
    if(any(df[column].isna())):
        null_col_list.append(column)
    else:
        continue
print(null_col_list)


# <br> Now that we have found the columns having the missing value, we can proceed how to deal with the data. We observe that we can replace all the missing values with their resepctive column's mean value except for `num-of-doors`. So we replace the missing doors with 4 and the rest of the values with the mean.

# In[6]:


df['normalized-losses'].replace(np.NaN, df['normalized-losses'].astype('float').mean(axis = 0), inplace = True)
df['bore'].replace(np.NaN, df['bore'].astype('float').mean(axis = 0), inplace = True)
df['horsepower'].replace(np.NaN, df['horsepower'].astype('float').mean(axis = 0), inplace = True)
df['peak-rpm'].replace(np.NaN, df['peak-rpm'].astype('float').mean(axis = 0), inplace = True)
df['price'].replace(np.NaN, df['price'].astype('float').mean(axis = 0), inplace = True)
df['stroke'].replace(np.NaN, df['stroke'].astype('float').mean(axis = 0), inplace = True)


# <br>
# Now that we have taken care of the missing values in the dataframe, let's observe the datatypes of the columns and convert them to the appropriate data types.

# In[7]:


df.dtypes


# In[8]:


df[['bore', 'stroke', 'price', 'peak-rpm']] = df[['bore', 'stroke', 'price', 'peak-rpm']].astype('float')
df[['normalized-losses']] = df[['normalized-losses']].astype('int')


# In[9]:


df.dtypes


# In[10]:


display(df.head())


# In[13]:


get_ipython().system('jupyter nbconvert --to script my_notebook.ipynb')


# In[ ]:




