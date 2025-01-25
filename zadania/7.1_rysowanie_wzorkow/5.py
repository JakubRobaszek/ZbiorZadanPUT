# Napisz program drukujący na ekranie literę L złożoną z literek L. Wielkość litery A (jej szerokość,
# wysokość i grubość) wczytujemy z klawiatury. Przykładowa litera ma wymiary: grubość=4, wys=11, szer=8.
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLLLLLL
# LLLLLLLL
# LLLLLLLL
# LLLLLLLL
grubosc = int(input("Grubość: "))
wys = int(input("Wysokość: "))
szer = int(input("Szerokość: "))
for i in range(wys):
    if i < wys - grubosc:
        print('L' * grubosc)
    else:
        print('L' * szer)
