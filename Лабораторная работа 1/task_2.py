# TODO Найдите количество книг, которое можно разместить на дискете
V_all_in_mb = 1.44
V_all_in_b = 1.44 * 1024**2
V_one_symbol_in_b = 4

pages = 100
lines = 50
symbols_in_line = 25

V_one_book = V_one_symbol_in_b * symbols_in_line * lines * pages
quantity_books = V_all_in_b // V_one_book

print("Количество книг, помещающихся на дискету:", int(quantity_books))
