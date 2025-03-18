#!/usr/bin/env python
# coding: utf-8

# In[20]:


#3.a. Multiple arrays
#stack two arrays vertically
import numpy as np
lst1=[10,20,30,40,50]
lst2=[60,70,80,90,100]
a=np.array(lst1)
print("A array")
print("*"*20)
print("content of a",a)
print("dimension",a.ndim)
print("size",a.size)
print("Dtype",a.dtype)
print("shape",a.shape)
b=np.array(lst2)
print("*"*20)
print("B array")
print("*"*20)
print("content of b",b)
print("dimension of b",b.ndim)
print("size of b",b.size)
print("Dtype of b",b.dtype)
print("shape of b",b.shape)
print("*"*20)
#syntax
#obj=numpy.vstack([a,b])
c=np.vstack([a,b])
print("C array")
print("*"*20)
print("content of c\n",c)
print("dimension of c",c.ndim)
print("Dtype of c",c.dtype)
print("size of c",c.size)
print("shape of c",c.shape)


# In[3]:


#3.b. Multiple arrays
#stack two arrays vertically
import numpy as np
lst1=[10,20,30,40,50]
lst2=[60,70,80,90,100]
a=np.array(lst1)
print("A array")
print("*"*20)
print("content of a",a)
print("dimension",a.ndim)
print("size",a.size)
print("Dtype",a.dtype)
print("shape",a.shape)
b=np.array(lst2)
print("*"*20)
print("B array")
print("*"*20)
print("content of b",b)
print("dimension of b",b.ndim)
print("size of b",b.size)
print("Dtype of b",b.dtype)
print("shape of b",b.shape)
print("*"*20)
#syntax
#obj=numpy.vstack([a,b])
c=np.hstack([a,b])
print("C array")
print("*"*20)
print("content of c\n",c)
print("dimension of c",c.ndim)
print("Dtype of c",c.dtype)
print("size of c",c.size)
print("shape of c",c.shape)


# In[13]:


#c. get the common items btw two python numpy arrays
import numpy as np
lst1=[10,20,30,40,50,60]
lst2=[60,30,80,90,20,70]
a=np.array(lst1).reshape(2,3)
b=np.array(lst2).reshape(2,3)
print("*"*20)
print("A array")
print("*"*20)
print(a)
print("*"*20)
print("B array")
print("*"*20)
print(b)
ind=np.where(a==b)
print("Index position:",ind)
print("Common items between both the arrays",ind)
print(ind)
print(a[ind])


# In[15]:


#3.d. Delete the common items of the numpy arrays
import numpy as np
lst1=[10,20,30,40,50,60]
lst2=[60,30,80,90,20,70]
a=np.array(lst1)
b=np.array(lst2)
print("*"*20)
print("A array")
print("*"*20)
print(a)
print("*"*20)
print("B array")
print("*"*20)
print(b)
ind=np.where(a==b)
print("Index position:",ind)
print("Common items between both the arrays",ind)
print(ind)
print(a[ind])
res= np.delete(a,ind)
print(res)


# In[16]:


#3.e. Get the poition of common elements
#c. get the common items between two python numpy arrays
import numpy as np
lst1=[10,20,30,40,50]
lst2=[60,30,80,90,20]
a=np.array(lst1)
b=np.array(lst2)
print("*"*20)
print("A array")
print("*"*20)
print(a)
print("*"*20)
print("B array")
print("*"*20)
print(b)
ind=np.intersect1d(a,b)
print("Index position:",ind)


# In[17]:


#c. get the common items between two python numpy arrays
import numpy as np
lst1=[10,20,30,40,50]
lst2=[60,30,80,90,20]
a=np.array(lst1)
b=np.array(lst2)
print("*"*20)
print("A array")
print("*"*20)
print(a)
print("*"*20)
print("B array")
print("*"*20)
print(b)
ind=np.intersect1d(a,b)
print("Index position:",ind)
print("Common items between both the arrays")
print(ind)
#deleting common elements
res1=np.setdiff1d(a,ind)
res2=np.setdiff1d(b,ind)
print("After deleting:")
print(res1)
print(res2)


# In[ ]:




