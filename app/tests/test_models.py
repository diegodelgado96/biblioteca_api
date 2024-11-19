from app.models import Book

def test_book_model():
    book = Book(
        title="Test Book",
        author="Test Author",
        year=2024,
        isbn="123-456-789"
    )
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.year == 2024
    assert book.isbn == "123-456-789"