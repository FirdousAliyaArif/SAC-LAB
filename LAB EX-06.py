#!/usr/bin/env python
# coding: utf-8

# In[18]:


#5. Data cleaning
#a. Find the pos of the missing values in the numpy array
import numpy as np
salary=np.array([1000,2000,3000,4000,5000,2500,35000])
com=np.array([10,20,30,None,None,25,None])
print("*"*20)
print("salary")
print(salary)
print("*"*20)
print("comission")
print(com)
print("*"*20)
position=np.where(com==None)
print("The missing values' position are:",position)
print(position)


# In[12]:


#Data cleaning 
#a. Find the position 
salary=np.array([1000,2000,3000,4000,5000,6000,7000])
com=np.array([10,20,30,None,None,None,None])
newcom=np.where(com==None,0,com)
print("*"*20)
print("Replace all missing values with 0 in a numpy array")

print(newcom)
print("*"*20)
netsal=salary+newcom
print(netsal)


# In[19]:


#b. Drop the rows that contain a missing value from a numpy array
import numpy as np
lst=[[1,2,np.nan],[3,4,5],[6,7,8],[9,10,11]]
a=np.array(lst)
print("Numpy array")
print(a)
print("*"*20)
#syntax resobj=numpy.isnan(ndarrayobj)
#syntax any(pass axis)
print("*"*20)
print("Rows with missing values")
print(a[np.isnan(a).any(axis=1)])
#Dropping the rows with the missing values
print("Deletion of the rows with the missing values")
print(a[~np.isnan(a).any(axis=1)])


# In[20]:


#c.Find the if the numpy array has null values
lst=[[1,2,np.nan],[3,4,5],[6,7,np.nan],[9,10,np.nan]]
a=np.array(lst)
print(a)
#syntax
#numpy.isnan()
np.isnan(a)


# In[ ]:


#d.

