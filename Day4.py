import numpy as np

with open('Puzzle4') as f:
  data = f.readlines()
for i in range(len(data)):
  data[i] = data[i].strip('\n').strip('[').split('] ')
data = sorted(data, key = lambda x: x[0])
IDs =[]
calendar = np.zeros(shape=(len(data),7), dtype=np.int)
n=0
for i in range(len(data)):
  if data[i][1] == 'falls asleep':
    date = np.array(data[i][0][:10].split('-')).astype(np.int)
    Start = np.int(data[i][0][-2:])
    End = np.int(data[i+1][0][-2:])
    Duration = End -Start
    m = 1
    while data[i-m][1][:7] != 'Guard #':
      m +=1
    ID = np.int(data[i-m][1][7:].split(' ')[0])
    calendar[n] = ID, date[0], date[1], date[2], Start, Duration, End
    n +=1
calendar = calendar[~np.all(calendar == 0, axis=1)]
IdX = np.unique(calendar[:,0])
Tots = np.zeros(len(IdX))
for i in range(len(IdX)):
  subdata = np.where(calendar[:,0] == IdX[i])
  Tots[i] += calendar[subdata, -2].sum()
  
print 'The max sleep duration is from guard #', IdX[Tots.argmax()] 
Lax = np.where(calendar[:,0] == IdX[Tots.argmax()])[0]
Routine = np.zeros(60)
for j in range(len(Lax)):
    Routine[calendar[Lax[j], -3]: calendar[Lax[j], -1]] += 1 

print 'The most common minute of sleep from guard #', IdX[Tots.argmax()], ' is ', Routine.argmax() 
print 'The code is '  IdX[Tots.argmax()]* Routine.argmax()

Frq= np.zeros((len(IdX),60))
for i in range(len(IdX)):
  sleep = np.where(calendar[:,0] == IdX[i])[0]
  for j in range(len(sleep)):
    Frq[i, calendar[sleep[j], -3]: calendar[sleep[j], -1]] += 1 
m,n = np.where(Frq == Frq.max())
print 'the most frequently asleep guard is ', IdX[m[0]], ' on the minute ', n[0]
print 'the code is ',IdX[m[0]]*n[0]
