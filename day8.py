import numpy as np
with open('Puzzle8') as f:
    data = f.read().strip().split(' ')
data = map(int, data)
metadata = []
levels = [] #contains the thickness of each branch dynamically
branch = np.zeros(len(data)) # contains the levels of branching
todo = []
i = 0
met = 0
while i < len(data)-data[1]:
    if data[i]+data[i+1] == 0: #empty node
        i +=2
        print 'pop'
#    if len(todo) >0: #after each node there is one less to do
#        todo[-1] -= 1
    if data[i] > 0: #if node branching out
        branch[i+2:] +=1
        levels.append(data[i])
        todo.append(data[i+1]) # the metadata to append when all higher branch terminated
        i +=2

    else : #The local tip of the branch (header 0)
        met = data[i+1]
        for d in data[i+2:i+2+met]:
            metadata.append(d)
        levels[-1]-= 1 # one thichness of the tip of the branch thinner
        i += 2+met
        while levels[-1] == 0: #end of the branch
            branch[i:] -= 1
            for d in data[i: i+1+todo[-1]]:
                metadata.append(d)
            i+= todo[-1]
            todo.pop()
            levels.pop()

toolow = 22799
print sum(metadata)
