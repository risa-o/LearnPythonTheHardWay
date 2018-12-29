texas = {
	'square_miles': '268,597',
	'state_bird': 'Mockingbird',
	'capitol': {'name': 'Austin',
				'nickname': "Music Capital of the World"},
	'nickname': 'The Lone Star State',
	'top_3_cities': ["Austin", "San Antonio", "Lubbock"]
}

print(texas['capitol'])



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
print(print_book)