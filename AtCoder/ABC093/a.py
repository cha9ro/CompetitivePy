
# coding: utf-8

# In[25]:


s = input()


# In[29]:


dic = {'a': 0, 'b': 0, 'c': 0}


# In[30]:


for c in s:
    if c in dic:
        dic[c] += 1


# In[31]:


if dic['a'] == 1 and dic['b'] == 1 and dic['c'] == 1:
    print ('Yes')
else:
    print ('No')

