#!/usr/bin/env python
# coding: utf-8

# In[4]:


#General Program

knock=0
print(knock)
knock=knock+9
if knock>5:
    print("knock! "*9)
else:
    print("I don't want to knock your door!")


# In[8]:


#Variable_assignment in python is doneby using an = operator where as the variable name is given on the left side and the corresponging value is given in the right

#Whatever we write in print section will be diplayed on screen where thye syntax differs from Python 2 to Python 3
#Print 3 in Python 2
#Print(3)in Python 3

Variable_assignment_number=20000 #Variable_assignment
print(Variable_assignment)

Variable_assignment_String="Hey Sivani!"
print(Variable_assignment_String)

#Reassigning same variable to a different variable
#python evaluates the expression on the right-hand-side of the = , and then assigns that value to the variable on the left-hand-side.
Variable_assignment_number=100
print(Variable_assignment_number)

Variable_assignment_none=None
print(Variable_assignment_none)


# In[2]:


# Hash is used to comment things in python it is widely used for single line comment however for multi line comment we use /* */


#Arithmetic Operations

a=3
b=8
print(a+b,a-b,a*b,a/b,a//b,a**b)

#Indentation

#See how indentation works in python

a=10
if a>0:
    print("The value of a is greater than zero")
else:
    print("The value of a is less than zero")
print("This statement will be printed irrespective of if condition") #This is how indentation works

#The lines indented with four spaces below if condition are considered as that particular if block statements and they are in sync with the if condition however, the print written in last line doesn't have any other condition aligned to it as it is written out of if block without indentation


# In[12]:


#Strings should be given either in single or double quotation mark

a="Hey"
b='Sivani'
print(a,b)


# In[15]:


# * Operator
a="Sivani"
b=5
print(a*5) #As it is string it prints string given number of times
print(b*5) #As it is numeral it calculates and gives output
print("String "*7)


# In[5]:


#Python is case sensitive
a=2
b=8
#print(A*b)
print(-a) #negation
print(-3*8+2)
print(max(9,3,111))
print(min(56,45,33333))
print(abs(-777))#gives absolute value
print(abs(999.33))
print(abs(32))


# In[6]:


#Float int 
print(float(10))
print(int(889.888))
#Using int and float as functions and giving args inside them which can be converted accordingly
print(int('444')+444)
print(float('456.89')+44)


# In[ ]:


#Kaggle Python 1st exercise
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *
print("Setup complete! You're ready to start question 0.")


# In[1]:


# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)


# Check your answer
color = 'blue'
q0.check()


# In[ ]:


pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius=(diameter)/2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area=pi*(radius)**2
        
# Check your answer
q1.check()

