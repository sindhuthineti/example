#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 use numpy to generate an array of 25 random numbers
import numpy as np
rand_num = np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)


# In[2]:


#2 create an array of 20 lineraly spaced points
import numpy as np
np.linspace(1, 10)


# In[3]:


#3 Declare a numpy array values from 1 to 100......10*10
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr)


# In[4]:


#4 using previous matrix print 1,5,6 rows
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[1])
print(arr[5])
print(arr[6])


# In[5]:


#using previous matrix 3rd row to 10th matrix
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[3:11])


# In[6]:


#using the previous matrix 4th column to 8th
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[4:9])


# In[7]:


#7 print 3rd row 2nd coloum
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[3:6,2:9])


# In[8]:


#8 1000 random numbers
from random import seed
from random import randint
seed(1)
for _ in range(10):
    value = randint(0, 10)
    print(value)


# In[9]:


#9 mean,median,mode
import statistics


# In[10]:


statistics.mean([1,2,3,4,5,6,7,8,9,10])


# In[11]:


statistics.median([5,4,3,8,9,7])


# In[13]:


statistics.mode([4, 1, 2, 2, 3, 5])


# In[ ]:




