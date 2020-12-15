#!/usr/bin/env python
# coding: utf-8

# In[118]:


#random number generator to simulate k populations
#load random number generator 
import random

#import the file to append the random numbers to
k_pops=[]


# In[119]:


import sys
original_stdout=sys.stdout

with open('k_pops_test.txt','w') as new_file:
    sys.stdout=new_file
    print(f'Individual\ta\tb\tc\td\te\n')
    NUM=0
    while NUM < 10:
        a=round(random.uniform(0.000,1.000), 4)
        b=round(random.uniform(0.000,1-a), 4)
        c=round(random.uniform(0.000,(1-a)-b), 4)
        d=round(random.uniform(0.000,(1-a-b)-c), 4)
        e=round((1-a-b-c)-d, 4)

        print(NUM+1,'\t',a,f'\t',b,f'\t',c,f'\t',d,f'\t',e)
    
        NUM=NUM+1

sys.stdout=original_stdout

