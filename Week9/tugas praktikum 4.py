nilai = int(input("Masukkan jumlah elemen dalam array: "))
array = list(range(1, nilai + 1))
print(f"Data array: {array}")

bilangan = int(input("Masukkan kelipatan yang ingin10 ditampilkan: "))

kelipatan = [x for x in array if x % bilangan == 0]

if kelipatan:
    print(f"Elemen yang merupakan kelipatan dari {bilangan}: {kelipatan}")
else:
    print(f"Tidak ada kelipatan dari {bilangan}.")