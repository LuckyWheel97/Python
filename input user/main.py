# data yang dinasukan pasti string
data = input("Masukan data: ")
print("Data = ", data,",type =", type(data))

# jika iingin mengambil data integer, maka
angka = int(input("Masukan data angka: "))
angka = float(input("Masukan data angka: "))

print("Data = ", angka,",type =", type(angka))

# jika ingin mengambil data boolean, maka
biner = bool(int(input("Masukan data biner: "))) # karena data yang dimasukan pasti string, maka harus diubah ke integer terlebih dahulu baru ke boolean

print("Data = ", biner,",type =", type(biner))