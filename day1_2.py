import numpy as np
data = np.genfromtxt('Puzzle1')
looper = True
l = np.cumsum(data)
n=0
while looper:
     a = l[-1]
     n += 1
     for j in range (len(l)):
         if l[j] in l[:j]:
             print 'found it! it is ',l[j], '\nDepth = ', n
             looper = False
             break
     l = np.hstack((l,l+a))
