# TODO Найдите количество книг, которое можно разместить на дискете

amount_of_symbol_bytes = 4  # В байтах
count_of_symbols = 25  # Кол-во символов в строке
count_of_lines = 50  # Кол-во строк на странице
count_of_pages = 100  # Кол-во страниц в книге

Total_volume_mb = 1.44
Total_volume_kb = Total_volume_mb * 1024
Total_volume_b = Total_volume_kb * 1024

Volume_1_book = count_of_pages * count_of_lines * count_of_symbols * amount_of_symbol_bytes

Count_all_books = Total_volume_b // Volume_1_book
Count_all_books = int(Count_all_books)

print("Количество книг, помещающихся на дискету:", Count_all_books)
