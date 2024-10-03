x = [ ]
for i in range(1, 10):
	y = [ ]
	for j in range(1, 10):
		y.append(str(i*j)+(3 - len(str(i*j)))*' ')
	x.append(y)
for i in range(9):
	print(*x[i], end = '\n\n')
	
	