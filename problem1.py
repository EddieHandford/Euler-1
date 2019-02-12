# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("hello world!")


#experiment 1
x = []
a = range(1,1000)
for i in a:

    if i%3 == 0 or i%5 == 0 :
      x.extend([i])


print (x)
total = sum (x)
print(total)
        


print("Task 1 complete")