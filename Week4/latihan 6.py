#Membuat Program Batu Gunting Kertas
orang1 = input ("Pilih Batu Gunting atau Kertas :")
orang2 = input ("Pilih Batu Gunting atau Kertas :")
orang1 = orang1.lower()
orang2 = orang2.lower()

seri = "Wah Seri Nih!" 
orang1_win = "Player 1 Menang!"
orang2_win = "Player 2 Menang!"
error = "Sepertinya Kamu Salah Input"

if orang1 == "batu":
    if orang2 == "batu":
        print(seri)
    elif orang2 == "kertas":
        print(orang2_win) 
    elif orang2 == "gunting":
        print(orang1_win)
elif orang1 == "gunting" :
    if orang2 == "gunting" :
        print(seri)
    elif orang2 == "batu" :
        print(orang2_win)
    elif orang2 == "kertas" :
        print(orang1_win)
elif orang1 == "kertas" :
    if orang2 == "kertas" :
        print(seri)
    elif orang2 == "batu" :
        print(orang1_win)
    elif orang2 == "gunting" :
        print(orang2_win)
else :
    print(error)