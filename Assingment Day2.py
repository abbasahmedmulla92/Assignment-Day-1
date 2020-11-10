#!/usr/bin/env python
# coding: utf-8

# # Question 1.

# In[1]:


lst= []

for i in range(0,10):
    x = int(input("\nEnter the value : "))
    lst.append(x)
    
even_lst = []

for i in lst:
    if(i%2==0):
        even_lst.append(i)
        
print("\nThe even list",even_lst)


# # Question 2.

# In[7]:


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# list comprehensions
num_lst = [i for i in lst if i%2==0 ]

print(num_lst)


# # Question 3.

# In[6]:


dict={}
n = int(input())
for i in range(1,n+1):
  dict[i] = i*i

print(dict)


# # Question 4.

# In[5]:


#  origin positions
pos = {"x":0,"y":0}

# getting movement input
n = int(input())

for i in range (n):
    move =  input().split(" ")
    
    if move[0].lower() == "up":
        pos["y"] += int(move[1])    
    
    elif move[0].lower() == "down":
        pos["y"] -= int(move[1])
    
    elif move[0].lower() == "left":
        pos["x"] -= int(move[1])
    
    elif move[0].lower() == "right":
        pos["x"] += int(move[1])

print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)))


# In[ ]:




