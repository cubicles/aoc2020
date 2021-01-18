#!/usr/bin/env python
# coding: utf-8

# # Day 1

# ## Part 1

# In[86]:


#Reading inputs
with open('inputs/day1.txt') as f:
    input = f.readlines()
numlist=[]
for i in input:
    numlist.append(int(i.split("\n")[0]))


# In[87]:


#First part
def day1part1(input):
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            sum = input[i]+input[j]
            if sum == 2020:
                answer = input[i]*input[j]
    return answer


# In[88]:


print(day1part1(numlist))


# ## Part 2

# In[89]:


#Second part
def day1part2(input):
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            for k in range(i+2,len(input)):
                sum = input[i]+input[j]+input[k]
                if sum == 2020:
                    answer = input[i]*input[j]*input[k]
    return answer


# In[90]:


print(day1part2(numlist))


# In[79]:


get_ipython().system('jupyter nbconvert --to script day1.ipynb')


# In[ ]:




