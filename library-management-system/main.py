class Book:

	def __init__(self, isbn, title, author):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.is_available = True


class Member:

	def __init__(self, id, name, books):
		self.id = id
		self.name = name
		self.books = books
		self.available_rentals = 3

class Library:

	def __init__(self):
		self.books = {}
		self.members = {}

	def add_member(self, member):
		pass



	