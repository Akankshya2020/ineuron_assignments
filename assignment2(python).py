#!/usr/bin/env python
# coding: utf-8

# In[4]:


rows = int(input("Enter the number of rows: ") )
  
# Outer loop will print the number of rows  
for i in range(0, rows):  
    # This inner loop will print the stars  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    # Change line after each iteration  
    print(" ") 
for i in range(rows + 1, 0, -1):  
    for j in range(0, i ):  
        print("*", end=' ')  
    print(" ")  


# In[5]:


s=str(input("input :  "))
def reverse(s):
    s=s[::-1]
    return s
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))


# In[ ]:




