angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

ganjil = []
genap = []

for num in angka:
    if num % 2 == 0:
        genap.append(num)
    else:
        ganjil.append(num)

total_ganjil = len(ganjil)
total_genap = len(genap)

print(f"Angka ganjil: {ganjil}")
print(f"Jumlah angka ganjil: {total_ganjil}")
print(f"Angka genap: {genap}")
print(f"Jumlah angka genap: {total_genap}")