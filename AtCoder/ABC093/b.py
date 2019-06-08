
# coding: utf-8

# In[37]:


line = input().split(' ')
A = int(line[0])
B = int(line[1])
K = int(line[2])


# In[38]:


for i in range(A, B+1):
    if (A <= i and i < A+K) or (B-K < i and i <= B):
        print (i)

