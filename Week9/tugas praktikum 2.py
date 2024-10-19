nilai = []

for i in range(5):
        while True:
            nil = float(input(f"Masukkan angka ke-{i+1}: "))
            nilai.append(nil) 
            print(f"{nilai}")
            break

total = sum(nilai)

while True:
    pilihan = input('Pilih jumlah atau rata - rata: ').lower()
    
    if pilihan == "jumlah":
        print(f"Jumlah total dari nilai data adalah: {total}")
        break
    elif pilihan == "rata-rata":
        rata_rata = total / len(nilai)
        print(f"Rata-rata dari nilai data adalah: {rata_rata}")
        break
    else:
        print('Input tidak valid! Silakan ketik "jumlah" atau "rata-rata".')