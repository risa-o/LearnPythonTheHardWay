
def while_loop(until):
	i = 0
	numbers = []
	while i < until:
		print(f"At the top, i is {i}")
		numbers.append(i)

		i += 1

		print("Numbers now: ", numbers)
		print(f"At the bottom, i is {i}")

	print("The numbers:  ")

	for num in numbers:
		print(num)

while_loop(9)