# Napisz program drukujący na ekranie literę A złożoną z literek A. Wielkość litery A wczytujemy z
# klawiatury.
#      A
#     A A
#    A   A
#   AAAAAAA
#  A       A
# A         A
size = int(input("Podaj wielkość litery A: "))
for i in range(size):
    if i == size // 2:
        print(' ' * (size - i - 1) + 'A' * (2 * i + 1))
    elif i < size // 2:
        print(' ' * (size - i - 1) + 'A' + ' ' * (2 * i - 1) + ('A' if i > 0 else ''))
    else:
        print(' ' * (size - i - 1) + 'A' + ' ' * (2 * i - 1) + 'A')