#Make a new file named book_dictionaries.py

#Write a new file name dictionaries.py

#Create a varaible `texas` and assign it to be a dictionary and set the following keys: square_miles, state_bird, capitol, nickname.
#Print out the texas variable.

#texas = {
#	'square_miles': '268,597',
#	'state_bird': 'Mockingbird',
#	'capitol': {'name': 'Austin',
#				'nickname': "Music Capital of the World"},
#	'nickname': 'The Lone Star State',
#	'top_3_cities': ["Austin", "San Antonio", "Lubbock"]
#}

#print(texas['capitol'])


#Write a function named make_book(title, author, categories) 
#- that returns a dictionary with the title set as a key that sets a string value, 
#- the author set as a key to a string value. 
#- If a list is not provided to categories, ensure that an empty list is assigned to the categories key (default parameter is empty list). 
#- Example: make_book("Deep Learning with Python", "Chollet", ["python", "deep learning"]) returns {'title': 'Deep Learning with Python', author': 'Chollet', categories: ['python', 'deep learning']}. 
#- Example: make_book("Bible", "buncha dudes") should return {'title': 'Bible', 'author': 'buncha dudes'}


def make_book(title, authors, categories):
	book = {}
	book['title'] = title
	book['authors'] = authors
	book['categories'] = categories
	return book

title = "Deep Learning with Python"
authors = "Chollet"
categories = ['python','deep learning']
print_book = make_book(title,authors,categories)


# Write a function named add_category_to_book(book, category) that takes 
# in a dictionary containing a "book" and a new category to add to that book's category list. 
def add_category(book,new_category):
	return book['categories'].append(new_category)

add_category(print_book,'self-help')
print(print_book)
# Using the make_book function, assign 3 new variables each containing their own "book" dictionaries. 
book1 = make_book("search for meaning", "victor henkyl", ["history","psychology","self-help"])
book2 = make_book(title,authors,categories)
book3 = make_book(title,authors,categories)

# Now make a variable named books that is a dictionary. 
#The only key is "books" and the value of this dictionary is a list containing all 5 of the books you previously defined. 
#Example: books = {'books': [bible, where_the_sidewalk_ends, giving_tree]} where the values on the list are previously defined dictionaries.

books = {
		'books': [print_book, book1, book2, book3] 
}

# Write a function named books_report that takes in the "books" dictionary as its input.
# The books_report should return a dictionary with the following keys and appropriately calculated values: 
# - Each key should be a defined category on at least one of the books. No duplicated keys. 

# The value for each key should be a list containing titles of each of the books that have that category. 
# For books with no category, ensure that there is a "no_category" key.
def books_report(books):
	all_categories = []
	output= {}
	for book in books['books']:
		all_categories.extend(book['categories'])
	unique_categories = set(all_categories)
	unique_categories_list = list(unique_categories)
	for category in unique_categories_list:
		output[category] = []
		for book in books['books']:
			if category in book['categories']:
				output[category].append(book['title'])
	return output

print(books_report(books))