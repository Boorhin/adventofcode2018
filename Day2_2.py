import numpy as np

def diff(Str1, Str2):
  ret = 0
  for i, j in zip(Str1, Str2):
    if i != j:
         ret +=1
    else:
         ID+=i
  if ret == 1:
    print Str1, Str2, '\nID =', ID
 
for i in range(len(lett)):
  for j in range(i, len(lett)):
    diff(lett[i], lett[j])
