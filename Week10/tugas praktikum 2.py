matriks = []

for a in range(2):
    matriks.append([])
    for b in range(3):
        matriks[a].append(int(input(f"Masukkan nilai ke-[{a}][{b}]: ")))

for a in range(2):
    for b in range(3):
        print(matriks[a][b], end= ' ')
    print()