import numpy as np
def Seek(L,  letter):
    IdX = []
    for i in range(len(L)):
        if L[i] == letter:
            IdX.append(i)
    return IdX

with open('Puzzle7') as f:
    data = f.readlines()
Ls, Le = [], []
for i in range(len(data)):
    Ls.append(data[i][5])
    Le.append(data[i][-13])
Alpha = np.ma.array([chr(x) for x in range(65, 91)])
letters = np.ma.copy(Alpha)
for l in Alpha:
    if l not in Le:
        Start=l
        break
#letters[np.where(letters == Start)[0]] = np.ma.masked


Ls, Le = np.ma.array(Ls), np.ma.array(Le)
DynS, DynE = np.copy(Ls), np.copy(Le)
#DynS[np.where(Ls == Start)[0]] = np.ma.masked
#DynE[np.where(Ls == Start)[0]] = np.ma.masked
Stack = ''
Forward = []
while len(Stack) <26:
    # if len(Stack) >0:

    Forward.sort()
    #     print Stack[-1], Forward
    for i in range(len(Alpha)):
        if letters[i]:
            if (letters[i] in Forward)  or (letters[i] not in DynE):
    #            print letters[i], len(DynS[Seek(DynE, letters[i])])
                Stack += Alpha[i]
                letters[i] = np.ma.masked
                Forward.extend(DynE[Seek(DynS, Stack[-1])])# break
    # if Alpha[i] in Forward:
    #     Forward.remove(Alpha[i])
    # else :
    #     print 'burp'
    for i in np.where(Le == Stack[-1])[0]:
            DynS[i] = np.ma.masked
            DynE[i] = np.ma.masked

print Stack
