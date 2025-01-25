# Napisz program drukujący na ekranie prostokąt z literek X. Wysokość i szerokość prostokąta wczytujemy z
# klawiatury. Poniższy prostokąt ma wymiary: szer=10, wys=4.
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
wys = int(input("Wysokość: "))
szer = int(input("Szerokość: "))
for i in range(wys):
    print('X' * szer)
