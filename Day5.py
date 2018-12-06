def SandD(data):
	i = 1
	Stack = [data[0]]
	while i < len(data):
		if Stack and Stack[-1] != data[i].swapcase():
			Stack.append(data[i])			
		else:
			try :
				Stack.pop()
			except:
				Stack.append(data[i+1])
				i += 1
		i += 1
	return len(Stack)

FName = 'Puzzle5'
Lengths =[]
letters = 'abcdefghijklmnopqrstuvwxyz'	

with open(FName) as f:
	D = f.read().strip('\n')
	   
for letter in letters:
	data = D.replace(letter,'').replace(letter.upper(),'')
	l = SandD(data)
	Lengths.append(l)
	print 'the length of the polymer without the ', letter, 'chain is ' , l
print 'the shortest polymer is ', min(Lengths)
