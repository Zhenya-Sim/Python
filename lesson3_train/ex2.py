from book import Book

myBooks = [
    Book("Мастер и Маргарита", "М.А.Булгаков"),
    Book("Гарри Поттер и узник Азкабана", "Д.Роулинг"),
    Book("Тринадцатая сказка", "Д.Сеттерфилд")
]

for book in myBooks:
    print(f"{book.name}, {book.author}")
