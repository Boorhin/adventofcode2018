import numpy as np
with open('Puzzle8') as f:
    data = f.read().strip().split(' ')
data = map(int, data)
metadata = []
levels = []
branch = np.zeros(len(data))
todo = []
i = 0
met = 0
while i < len(data)-data[1]:
    if len(todo) >0 :
        todo[-1] -= 1 #print i, todo
    if data[i] > 0:
        branch[i+2:] +=1
        levels.append(data[i])
        todo.append(data[i+1])
        i +=2
        #print levels, todo
    else :
        met = data[i+1]
        for d in data[i+2:i+2+met]:
            metadata.append(d)
        levels[-1]-= 1
        i += 2+met
        #print levels, todo
        if levels[-1] == 0:
            #print 'here'
            branch[i:] -= 1
            for d in data[i: i+1+todo[-1]]:
                metadata.append(d)
            i+= todo[-1]
            todo.pop()
            levels = levels[:-1]

toolow = 19500
print sum(metadata)
