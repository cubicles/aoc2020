#!/usr/bin/env python
# coding: utf-8

# # Day 3

# ## Part 1

# In[19]:


#Reading inputs
with open('inputs/day3.txt') as f:
    input = f.readlines()
list=[]
for i in input:
    list.append(i.split("\n")[0])


# In[20]:


#First part
def day3part1(input):
    count = 0
    j=0
    for i in range (0,len(input)):
        k=j%(len(input[0]))
        evaluator = input[i][k]
        if evaluator == "#":
            count = count + 1
        j=j+3    
        #print(i,k)
    return count


# In[21]:


day3part1(list)


# ## Part 2

# In[22]:


#Second part
def day3part2(right,down,input):
    count = 0
    j=0
    for i in range (0,len(input),down):
        k=j%(len(input[0]))
        evaluator = input[i][k]
        if evaluator == "#":
            count = count + 1
        j=j+right    
        #print(i,k)
    return count


# In[23]:


case_1 = day3part2(1,1,input3)
case_2 = day3part2(3,1,input3)
case_3 = day3part2(5,1,input3)
case_4 = day3part2(7,1,input3)
case_5 = day3part2(1,2,input3)
print(case_1*case_2*case_3*case_4*case_5)


# In[24]:


get_ipython().system('jupyter nbconvert --to script day3.ipynb')


# In[ ]:




