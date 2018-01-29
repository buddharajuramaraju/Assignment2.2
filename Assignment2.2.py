
# coding: utf-8

# ### Problem Statement
# 
# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[1]:


list1 = [x for x in 'ACADGILD']
print(list1)


# In[5]:


list2 = [x*y for x in ['x','y','z'] for y in range(1,5)]
print(list2)


# In[7]:


list3 = [x*y for x in range(1,5) for y in ['x','y','z']]
print(list3)


# In[9]:


list4 = [[x+y] for x in range(1,4) for y in range(1,4)]
print(list4)


# In[18]:


list5 = [[x+z for x in range(1,5)] for z in range(1,5)]
print(list5)


# In[19]:


list4 = [(x,y) for x in range(1,4) for y in range(1,4)]
print(list4)

