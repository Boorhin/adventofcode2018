import numpy as np
def Seek(L,  letter):
    IdX = []
    for i in range(len(L)):
        if L[i] == letter:
            IdX.append(i)
    return IdX
def addup(l, letters, DynS, DynE):
    letters[np.where(letters==l)[0]] = np.ma.masked
    for j in np.where(DynE == l)[0]:
        if DynS[j] == l:
            DynS[j] = np.ma.masked
            DynE[j] = np.ma.masked
    return letters, DynS, DynE

with open('Puzzle7') as f:
    data = f.readlines()
Ls, Le = [], []
for i in range(len(data)):
    Ls.append(data[i][5])
    Le.append(data[i][-13])
Alpha = np.ma.array([chr(x) for x in range(65, 91)])
letters = np.ma.copy(Alpha)
letters.mask=np.zeros(26)
Ls, Le = np.ma.array(Ls), np.ma.array(Le)
DynS, DynE = np.ma.copy(Ls), np.ma.copy(Le)
DynS.mask, DynE.mask=np.zeros(len(DynS)),np.zeros(len(DynS))
Stack = []
while len(Stack) <26:
    for i in range(len(Alpha)):
        if not letters.mask[i]:
            l = letters[i]
            check = True
            while check:#check all tasks completed for work
                for j in DynS[Seek(DynE,l)]:
                    if j in Stack:
                        task = True
                    else:
                        task = False
                        check = False
                check = False
            if (l not in DynE) or task:
                Stack.append(l)
                letters, DynS, DynE = addup(l, letters, DynS, DynE)
x = ''
for s in Stack:
     x += s
print x
