#!/usr/bin/env python
# coding: utf-8

# # Day 1

# ## Part 1

# In[20]:


#Reading inputs
with open('inputs/day2.txt') as f:
    input = f.readlines()
list=[]
for i in input:
    list.append(i.split("\n")[0])


# In[23]:


#First part
def day2part1(input):
    count = 0
    for i in range(len(input)):
        element = input[i]
        lower_bound = int(input[i].split("-")[0])
        higher_bound = int(input[i].split("-")[1].split(" ")[0])
        evaluator = input[i].split(" ")[1][0]
        evaluation = input[i].split(" ")[2]
        validator = evaluator in evaluation
        if validator != 0:
            c = evaluation.count(evaluator)
            first = (c>= lower_bound)
            second = ((c<= higher_bound))
            if c >= lower_bound and c<= higher_bound:
                count = count + 1
    return count


# In[24]:


day2part1(list)


# ## Part 2

# In[25]:


#Second part
def day2part2(input):
    count = 0
    for i in range(len(input)):
        element = input[i]
        lower_bound = int(input[i].split("-")[0])
        higher_bound = int(input[i].split("-")[1].split(" ")[0])
        evaluator = input[i].split(" ")[1][0]
        evaluation = input[i].split(" ")[2]
        validator = evaluator in evaluation
        if lower_bound in range(len(evaluation)+1):
            first = evaluation[lower_bound-1] == evaluator
        else:
            first = False
        if higher_bound in range(len(evaluation)+1):
            second = evaluation[higher_bound-1] == evaluator
        else:
            second = False
        if first != second:
            count = count + 1
    return count


# In[26]:


day2part2(list)


# In[28]:


#!jupyter nbconvert --to script day2.ipynb


# In[ ]:




