print("Hello, World!")

# ini adalah komen pada 

# kita bisa mengcompile python ke
# yang namanya bytecode 
# cara mengcompile, buka terminal dan ketik
# python3 -m py_compile main.py

# VARIABLE
# variable adalah tempat untuk menyimpan data
 # a adalah variable yang menyimpan data 10
 # = adalah operator assignment untuk memberikan nilai ke variable
 # 10 adalah value atau nilai yang disimpan dalam variable a
 
a = 10 
x = 5
panjang = 1000

# pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# penamaan
nilai_y = 20 # harus mengguanakan underscore untuk memisahkan kata
juta10 = 10000000 # tidak boleh diawali dengan angka
nilaiZ = 30 # boleh menggunakan huruf kapital untuk memisahkan kata, tapi tidak disarankan

# pemanggilan kedua
print("Nilai a = ", a)
a = 5 # kita bisa mengubah nilai variable a menjadi 5
print("Nilai a = ", a) # nilai a sekarang adalah 5

# assigment indierect
b = a # variable b sekarang menyimpan nilai yang sama dengan variable a
print("Nilai b = ", b) # nilai b adalah 5, karena menyimpan

# TIPE DATA
# tipe data adalah jenis data yang bisa disimpan dalam variable
# a = 10, a adalah variable dengan nilai 10

# tie data: angkasatuan yang tidak ada komanya
data_integer = 10
print("Data :", data_integer)
print("-- Bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("Data :", data_float)
print("-- Bertipe : ", type(data_float))

# tipe data: teks (string)
data_string = "Hello, World!"
print("Data :", data_string)
print("-- Bertipe : ", type(data_string))

# tie data: biner true/false (boolean)
data_boolean = True
print("Data :", data_boolean)
print("-- Bertipe : ", type(data_boolean))

## tipe data khusus
# bilangan kompleks
data_complex = complex(2,3) # bilangan kompleks dengan bagian real 2 dan bagian imajiner 3
print("Data :", data_complex)
print("-- Bertipe : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(3.14) # tipe data double dari bahasa C
print("Data :", data_c_double)
print("-- Bertipe : ", type(data_c_double))





### Casting tipe data adalah merubah dari satu tipe data ke tipe data lain

