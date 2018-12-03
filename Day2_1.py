import numpy as np
lett = np.genfromtxt('Puzzle2')
n2, n3 = 0,0
for i in range(len(lett)):
    a, c = np.unique(np.array(list(lett[i])), return_counts=True)
    n2 += np.count_nonzero(c==2)
    n3 += np.count_nonzero(c==3)
print('the number of doublon is ', n2)
print('the number of triplets is ', n3)
print('the checksum is ', n2*n3)
