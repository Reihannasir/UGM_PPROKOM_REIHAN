#Membuat program untuk menampilkan siswa yang lulus dan tidak lulus
nama = input("Nama Siswa = ")
nilai = int(input("Nilai Ujian = "))
lulus = "Selamat Anda Lulus Ujian :)"
tidak_lulus = "Maaf, Anda Tidak Lulus Ujian\nTetap Semangat dan Jangan Menyerah!"

if(nilai >= 70) :
        print()
        print(lulus)
else :
        print()
        print(tidak_lulus)