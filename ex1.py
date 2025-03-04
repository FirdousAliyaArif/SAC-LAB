#!/usr/bin/env python
# coding: utf-8

# In[15]:


#working with arrays
#create a 1D array
import numpy as np
nd=np.random.randint(1,100,size=10)
print("1D data")
print("content of nd",nd)
print("type od nd",type(nd))
print("dtype of nd",nd.dtype)
print("shape of nd",nd.shape)
print("dimension of nd",nd.ndim)
print("size of nd",nd.size)


# In[4]:


#b. create a boolean array
lst=[0,1,2,3,4,5,6,7,8]
ndo=np.array(lst,dtype=bool)
print(ndo)
ndo=ndo.reshape(3,3)
print(ndo)
print("dimension",ndo.ndim)
print("dtype",ndo.dtype)
print("shape",ndo.shape)
print("size",ndo.size)


# In[6]:


#c. extract items that satisfy a given condition
import numpy as np
ndo=np.random.randint(1,10,size=10)
print(ndo)
index=np.where(ndo>5)
print(index)
print(ndo[index])


# In[7]:


#d. replace items that satify a condition with another value in the numpy array
ts=[10,20,15,18,25,70,56]
ap=[25,19,30,45,7,89,90]
t=np.array(ts)
a=np.array(ap)
poll=np.where(t>18,t,a)
print(poll)


# In[16]:


#e. replace items that satisfy a condition without affectiong the orignal array
sal=np.array([1000,2000,3000,4000,5000,6000])
comission=np.array([10,20,30,None,None,None])
newsal=np.where(comission==None,0,comission)
print(newsal)
netsal=sal+newsal
print("new salary")
print(netsal)


# In[17]:


#f. reshape an array
ndo=np.random.randint(1,50,size=(3,3))
print(ndo)
nd1=ndo.reshape(9,)
print(nd1)


# In[18]:


#g. extract all numbers between a given range from a numoy array
ndo=np.random.randint(5,10,size=8)
print(ndo)
out=np.extract(ndo>5,ndo)
print(out)


# In[20]:


#Binary file saving
import numpy as np
lst=[10,20,30,40,50,60]
i=np.array(lst)
res=np.save("out",i)
print("file is saved successfully...")


# In[21]:


#binary file.load
res=np.load("out.npy")
print("file is loaded successfully")
print(res)


# In[22]:


lst=[100,200,300,400,500]
a=np.array(lst)
res=np.savetxt("outt.txt",a)
print("my txt file is saved successfully....")
print(res)


# In[ ]:


lst=[15,25,50,75,100]
c=np.array(lst)
res=np.savetxt("outt.")

