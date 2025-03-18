#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Binary file saving
import numpy as np
lst=[10,20,30,40,50,60]
i=np.array(lst)
res=np.save("out",i)
print("file is saved successfully...")


# In[2]:


#binary file.load
res=np.load("out.npy")
print("file is loaded successfully")
print(res)


# In[3]:


#saving a text file
lst=[100,200,300,400,500]
a=np.array(lst)
res=np.savetxt("outt.txt",a)
print("my txt file is saved successfully....")
print(res)


# In[9]:


#Loading the text file
lst=[15,25,50,75,100]
c=np.array(lst)
res=np.savetxt("outt.

