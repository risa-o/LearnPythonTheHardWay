# list_enumeration.py

# Lesson Number 1
# Given
fruits = ["mango", "banana", "kiwi", "guava", "pineapple"]

# enumerate lets us use "i, value" syntax to access the indices of data
# "for i, fruit in fruits" is nonsense without enumerate() around fruits.
for i, fruit in enumerate(fruits):
    print("the fruit at index ", i, " is ", fruit)
    print("fruits[i] is another way to access", fruit)
    print(fruits[i])
    print(fruit)

# Walkthrough #1, let's find the index of the fruit with the longest string
longest = "" #because the length of all other fruit strings should be compared to empty string w/ zero character length
index_of_longest = None #because we don't know this value yet.
for i, fruit in enumerate(fruits):
    if len(fruit) > len(longest):
        longest = fruit
        index_of_longest = i

print(longest)
print("The index of the string with the most characters is ", i)
print(fruits[i])


# Lesson number 2

# Given:
items = [
    "id, title, quantity",
    "1, hammer, 2",
    "2, screwdriver, 3",
    "3, shingles, 10"
]

# now we have to lose the headers, so let's do this
headers = items[:1] # assigns the list of strings "id", "title", and "quantity"
items = items[1:] #assigns the list of strings to items variable without the headers

for i, item in enumerate(items):
    print("The string at index ", i, " is ", item)\

# How would we add up the total number of items above?
total = 0
for item in items:
    item_details = item.split(", ")
    item_id = item_details[0]
    item_name = item_details[1]
    item_quantity = item_details[2]
    total += int(item_quantity) #plus equals is shorthand for total = total + item_quantity

# How would we get the index of the string with the highest quantity?
index_we_want = None 
highest = 0
for i, item in enumerate(items):
    item_details = item.split(", ")
    print(item_details)

    item_quantity = int(item_details[2])
    if item_quantity > highest:
        highest = item_quantity
        index_we_want = i

print("The index of the string with the highest quantity is ", index_we_want)
print(items[index_we_want])
print("and that item's name is: ", items[index_we_want].split(", ")[1])