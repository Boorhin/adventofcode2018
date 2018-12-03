import numpy as np
fab = np.genfromtxt('Puzzle3', dtype =np.int)
max_width  = fab[:,1]+fab[:,3]
max_heigth = fab[:,2]+fab[:,4]
carpet = np.zeros(shape=(max_heigth.max(), max_width.max()))
for i in range(len(fab)):
  carpet[fab[i,2]:fab[i,2]+fab[i,4], fab[i,1]:fab[i,1]+fab[i,3]] +=1
print 'the number of common sqinches is ', len(np.where(carpet>1)[0])
for i in range(len(fab)):
  if carpet[fab[i,2]:fab[i,2]+fab[i,4], fab[i,1]:fab[i,1]+fab[i,3]].sum() == fab[i,4]*fab[i,3]:
    print 'the ID is ', i+1
