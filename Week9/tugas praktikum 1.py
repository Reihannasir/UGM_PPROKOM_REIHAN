nilai_mahasiswa = []

while True:
    print("\nMenu:") 
    print("1. Tambahkan data nilai mahasiswa") 
    print("2. Tampilkan semua data nilai mahasiswa") 
    print("3. Tampilkan data nilai mahasiswa yang memiliki nilai tertinggi") 
    print("4. Keluar") 
    pilihan = int(input("Masukan pilihan:"))
    
    if pilihan == 1:
        nilai = int(input("Masukan nilai mahasiswa:"))
        nilai_mahasiswa.append(nilai)
        print("Data nilai mahasiswa yang telah ditambahkan:", nilai_mahasiswa)
    elif pilihan == 2:
        if nilai_mahasiswa:
            print("Semua data nilai mahasiswa:", nilai_mahasiswa)
        else:
            print("Data nilai mahasiswa maish kosong")
    elif pilihan == 3:
        if nilai_mahasiswa:
            print("Data nilai mahasiswa yang memiliki nilai tertinggi:", max (nilai_mahasiswa))
        else:
            print("Data nilai mahasiswa masih kosong")
    elif pilihan == 4:
        break
