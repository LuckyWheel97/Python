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