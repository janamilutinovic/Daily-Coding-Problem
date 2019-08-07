#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Daily Coding Problem 


# In[34]:


#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the #original array except the one at i.

from functools import reduce
l = [1, 2, 3, 4, 5]
#l = [3, 2, 1]
x = reduce(lambda x, y : x*y ,l)
p = []

for i in l:
    p.append(x // i)

print(p) 


# In[ ]:




