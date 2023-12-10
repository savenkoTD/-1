data_disk_megabites = 1.44
one_symbol = 4
symb_in_line = 25
lines_on_list = 50
lists_in_book = 100
bites_in_book = one_symbol * symb_in_line * lines_on_list * lists_in_book
megabites_in_book = bites_in_book / (1024*1024)
count_of_books = int(data_disk_megabites//megabites_in_book)
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", count_of_books)
