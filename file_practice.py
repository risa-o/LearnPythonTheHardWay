filename = "data.txt"

with open (filename,"r") as file_object:
	contents = file_object.read()

print(contents)
print(type(contents))
lines = contents.split('\n')
print(type(lines))

#reassign lines or make a new variable: get rid of the 
#first name, last name, sales units called rows. (ditch the headers)

lines.pop(0)
print(lines)

total = 0

splitlines =  lines[0].split(', ')

print (splitlines[-1])
total += int(splitlines[-1])
print (total)
sales_total = 0

for line in lines:
	pieces = line.split(', ')
	sales_total += int (pieces[-1])
	
print(sales_total)