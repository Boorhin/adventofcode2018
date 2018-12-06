with open('Puzzle5') as f:
  data = f.read()
L = len(data)
Continue = True
while Continue:
  for i in range(len(data)-1):
      if data[i] == data[i+1].upper() or data[i].upper() == data[i+1]:
          data = data[:i]+data[i+2:]
  if len(data) != L:
      L = len(data)
  else:
      Continue = False  
