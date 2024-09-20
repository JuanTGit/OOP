
class Book:

	def __init__(self, title, author, year_published, isbn):
		self.title = title
		self.author = author
		self.year_published = year_published
		self.isbn = isbn

	def __str__(self):
		return f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}, ISBN: {self.isbn}"

class BookCatalog:
	def __init__(self):
		self.catalog = {}


	def add_book(self, book: Book):
		if book.isbn in self.catalog:
			print(f'Error: Book with ISBN {book.isbn} already exists.')
		else:
			self.catalog[book.isbn] = book
			print(f"Book '{book.title}' added to catalog")

	def get_book(self, isbn):
		if isbn in self.catalog:
			return str(self.catalog[isbn])
		return None
	
	def search_books(self, search_term: str, search_by: str):
		"""Search for books by title, author, or year."""
		res = []

		for isbn, book in self.catalog.items():
			if search_by == "title" and search_term.lower() in book.title.lower():
				res.append(str(book))
		return res

	def update_book(self, isbn: str, new_title=None, new_author=None, new_year=None, new_isbn=None):
		"""Update book information."""
		pass

	def delete_book(self, isbn: str):
		"""Delete a book from the catalog using its ISBN."""
		pass

		

catalog = BookCatalog()

book1 = Book("1984", "George Orwell", 1949, "12345")

catalog.add_book(book1)

# print(catalog.get_book('12345'))
print(catalog.search_books('19', 'title'))