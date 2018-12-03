import numpy as np
lett = np.genfromtxt('Puzzle2', dtype=np.str)
n2, n3, m, n = 0,0, 2,3
for i in range(len(lett)):
    a, c = np.unique(np.array(list(lett[i])), return_counts=True)
    if np.any(c==m):
        n2 +=1
    if np.any(c==n):
        n3 += 1
print('the number of doublon is ', n2)
print('the number of triplets is ', n3)
print('the checksum is ', n2*n3)
