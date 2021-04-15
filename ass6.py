#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1.fill null values of a data frame using median and mode

import numpy as np
import pandas as pd
df = pd.DataFrame({
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,np.nan,65.26,110.5,948.5,np.nan,5760,1983.43,np.nan,250.45, 75.29,3045.6],
'sale_amt':[10.5,20.65,np.nan,11.5,98.5,np.nan,57,19.43,np.nan,25.45, 75.29,35.6]})
print(df)


# In[10]:


df['sale_amt'].fillna(df['sale_amt'].mode(), inplace=True)
print(df)


# In[11]:


df['purch_amt'].fillna(df['purch_amt'].median(), inplace=True)
print(df)


# In[12]:


#Create a dataframe and add a column, add names in it using apply function to return names whose length is greater than 5
import pandas as pd
df = pd.DataFrame({'Date' : ['11/8/2011', '11/9/2011', '11/10/2011',
                                        '11/11/2011', '11/12/2011'],
                'Event' : ['Music', 'Poetry', 'Music', 'Comedy', 'Poetry']})
  
print(df)


# In[13]:


#4.create a numpy array and a dataframe and concatenate them
np.random.seed(0)
df = pd.DataFrame(np.random.choice(10, (3, 3)), columns=list('ABC'))
print(df)


# In[ ]:


#2.what is the difference between merging and joining in dataframe

Both join and merge can be used to combines two dataframes but the join method combines two dataframes on the basis of their indexes whereas the merge method is more versatile and allows us to specify columns beside the index to join on for both dataframes.
Merge:=
    The pd. merge() function recognizes that each DataFrame has an "employee" column, and automatically joins using this column as a key. The result of the merge is a new DataFrame that combines the information from the two inputs.
Join:=
    Join columns with other DataFrame either on index or on a key column. Efficiently join multiple DataFrame objects by index at once by passing a list.

