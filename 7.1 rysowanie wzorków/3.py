# Napisz program drukujący na ekranie prostokąt z literek X. Wysokość i szerokość prostokąta wczytujemy z klawiatury:
# XXXXXXXXXX
# X        X
# X        X
# XXXXXXXXXX
y = int(input("Podaj wysokość prostokąta: "))
x = int(input("Podaj szerokość prostokąta: "))
for i in range(y):
    if i == 0 or i == y-1:
        print('X' * x)
    else:
        print(f'X{" " * (x - 2)}X')