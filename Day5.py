import matplotlib.pyplot as plt
fig, ax = plt.subplots()

with open('Puzzle5') as f:
	data = f.read().strip('\n')
L = [len(data)]
i = 1
I = [i]
while i < len(data):
		host = len(data)
		if data[i-1] != data[i].swapcase():
			i += 1
		else:
			data = data[:i-1]+data[i+1:]
			i -= 1
			L.append(len(data))
			I.append(i)
print 'the length of the polymer is ', len(data)
ax.plot(L,I)
ax.set_xlabel('Polymer length')
ax.set_ylabel('verified units')
plt.show()
