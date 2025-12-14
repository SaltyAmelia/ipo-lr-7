# Мигунов
print("start code ...")

books = [
    {
        'title': '1984',
        'author': 'Джордж Оруэлл',
        'year': 1949
    },
    {
        'title': 'Гарри Поттер ',
        'author': 'Джоан Роулинг',
        'year': 1997
    },
    {
        'title': 'О дивный новый мир',
        'author': 'Олдос Хаксли',
        'year': 1932
    },
    {
        'title': 'Мастер и Маргарита',
        'author': 'Михаил Булгаков',
        'year': 1967
    },
    {
        'title': 'Автостопом по галактике',
        'author': 'Дуглас Адамс',
        'year': 1979
    }
]

count = 1
for book in books:    
    print( '-' * 50 + f"Книга {count}" +'-' * 50)
    print(f" Название: {book['title']}, Автор: {book['author']},")
    print ('-' * 50 , book['year'] , '-' * 50, end='\n\n')
    count += 1
print("... end code")