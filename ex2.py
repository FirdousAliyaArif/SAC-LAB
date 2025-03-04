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


# In[21]:


#b. get the common items between two python numpy arrays
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


# In[22]:


#4. Multidimensional arrays
#a. convert an array of arrays into flat 1d array
import numpy as np
a=np.random.randint(1,100,size=(4,3))
print("content of a",a)
for i in a:
    for j in i:
        print(j)


# In[38]:


import numpy as np
a=np.random.randint(1,100,size=(4,3))
print("Multidimensional array")
print("content of a",a)
print("Dimension of a",a.ndim)
print("dtype of a",a.dtype)
print("size of a",a.size)
print("shape of a",a.shape)
print("flat data or 1D")
print("*"*20)
b=a.reshape(12,)
print("one dimensional array")
print("content of b",b)
print("dimension of b",b.ndim)
print("dtype of b",b.dtype)
print("size of b",b.size)
print("shape of b",b.shape)
print("flat data or 1D")


# In[29]:


import numpy as np
a=np.random.randint(1,100,size=(3,3))
print(a)
a[:,[0,2]]=a[:,[2,0]]
print("*"*20)
print("After Swapping:")
print(a)


# In[33]:


#a. covert array into 1D
import numpy as np
a=np.random.randint(1,100,size=(4,3))
print("content of a\n",a)
b=a.reshape(12,)
print(b)


# In[ ]:




