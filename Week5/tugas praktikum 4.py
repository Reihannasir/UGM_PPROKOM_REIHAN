total_data = int(input("Masukan Jumlah Data :"))

if total_data <= 0:
        print("Jumlah data harus lebih dari 0.")
total = 0
    
for i in range(total_data):
        while True:
            try:
                nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
                total += nilai
                break
            except ValueError:
                print("Input tidak benar. Silahkan masukkan angka.")
        
rata_rata = total / total_data
    
print(f"Rata-rata dari {total_data} data adalah: {rata_rata}")