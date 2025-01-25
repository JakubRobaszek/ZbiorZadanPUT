# Napisz program drukujący na ekranie trójkąt. Wysokość trójkąta wczytujemy z klawiatury. Poniższy trójkąt
# ma wysokość wys=5.
#     X
#    XXX
#   XXXXX
#  XXXXXXX
# XXXXXXXXX
wys = int(input("Wysokość: "))
for i in range(1, wys + 1):
    print(' ' * (wys - i) + 'X' * (i * 2 - 1))
