import numpy as np

Coord = np.genfromtxt('Puzzle6', delimiter =', ', dtype=np.int)
maxX, maxY = 500, 500
host = np.zeros(shape=(len(Coord), maxY, maxX), dtype =np.int)
for i in range(len(Coord)):
		for j in range(maxY):
				host[i,j, Coord[i, 0]:] += range(maxX-Coord[i, 0])
				host[i,j, :Coord[i, 0]] += range(0, Coord[i, 0])[::-1]
		for k in range(maxX):
				host[i, Coord[i, 1]:, k] += range(maxX-Coord[i, 1])
				host[i, :Coord[i, 1], k] += range(0, Coord[i, 1])[::-1]		
map = np.ma.zeros(shape=(maxY, maxX), dtype =np.int)
for j in range (len(map)):
		for i in range(len(map[0])):
			Min  = np.min(host[:,j,i])
			IdX = np.where(host[:,j,i] == Min)[0]
			if len(IdX) <2 :
					map[j,i] = IdX
			else:
				map[j,i] = np.ma.masked

				
				
#Shrink
edges = np.unique(map[0]).data
edges = np.hstack((edges, np.unique(map[-1])))
edges = np.hstack((edges, np.unique(map[:,0])))
edges = np.hstack((edges, np.unique(map[:,-1])))

for v in edges:
	map = np.ma.masked_values(map, v)
a,b = np.unique(map, return_counts=True)

print 'the largest area is ', b[:-1].max()
