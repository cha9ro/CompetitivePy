
# coding: utf-8

# In[11]:


line = input().split(' ')
n = int(line[0])
c = int(line[1])


# In[19]:


x = [0] * n
v = [0] * n
for i in range(n):
    line = input().split(' ')
    x[i] = int(line[0])
    v[i] = int(line[1])


# In[20]:


d_clock = [0] * n
d_counter = [0] * n
d_clock[0] = x[0]
d_counter[0] = c - x[n-1]
for i in range(1, n):
    d_clock[i] = x[i] - x[i-1]
    d_counter[i] = x[n-i] - x[n-1-i]


# In[21]:


costClock = 0
costCounter = 0
scoreClock = [0] * n
scoreCounter = [0] * n
for i in range(n):
    costClock += v[i] - d_clock[i]
    scoreClock[i] = costClock
    costCounter += v[n-1-i] - d_counter[i]
    scoreCounter[i] = costCounter


# In[24]:


walkMax = max(max(scoreClock), max(scoreCounter))
print (max(0, walkMax))

