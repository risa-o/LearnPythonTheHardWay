def sumFromOneTo(entry):
	numlist = [0]
	i = 0
#	sum = 0
	while i < entry:
		numlist.append(i+1)
		i += 1
#	for num in numlist:
#		sum += num
	return sum(numlist)

entry = int(input("Enter a number:  "))
print(sumFromOneTo(entry))