#Nama file: nested_if_statement.py
jenis_kelamin = input("Jenis Kelamin = ")
umur = int(input("Masukan Umur= "))
if (jenis_kelamin=="Pria"):
 if (umur >= 25):
    print ("Pria boleh menikah")
 else:
    print ("Pria tidak boleh menikah")
elif(jenis_kelamin=="Wanita"):
 if (umur >= 20):
    print ("Wanita boleh menikah")
 else:
    print ("Wanita tidak boleh menikah")
else:
    print ("Jenis kelamin tidak terdaftar")