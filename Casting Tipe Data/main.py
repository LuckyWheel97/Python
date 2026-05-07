### Casting tipe data adalah merubah dari satu tipe data ke tipe data lain

##Integer
print("====== Integer =====")
data_int = 9;
print("data =", data_int, "type =", type(data_int))

data_float = float(data_int) # merubah data_int yang awalnya integer menjadi float
data_str = str(data_int) # merubah data_int yang awalnya integer menjadi string
data_bool = bool(data_int) # merubah data_int yang awalnya integer menjadi boolean
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))


## Float
print("====== Float =====")
data_float = 9.5;
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float) # merubah data_float yang awalnya float menjadi integer, akan dibulatkan ke bawah
data_str = str(data_float) # merubah data_int yang awalnya integer menjadi string
data_bool = bool(data_float) # merubah data_int yang awalnya integer menjadi boolean
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))


## Boolean
print("====== Boolean =====")
data_bool = True;
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool) # merubah data_bool yang awalnya boolean menjadi integer
data_str = str(data_bool) # merubah data_bool yang awalnya boolean menjadi string
data_float = float(data_bool) # merubah data_bool yang awalnya boolean menjadi float
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_float, "type =", type(data_float))

## String
print("====== String =====")    
data_str = "10"; # nilai string kosong makan akan bernilai false jika diubah ke boolean, selain itu akan bernilai true
print("data =", data_str, "type =", type(data_str))

data_int = int(data_str) # merubah data_str yang awalnya string menjadi integer
data_float = float(data_str) # merubah data_str yang awalnya string menjadi float
data_bool = bool(data_str) # merubah data_str yang awalnya string menjadi boolean, akan bernilai true jika string tidak kosong
print("data =", data_int, "type =", type(data_int))
print("data =", data_float, "type =", type(data_float))
print("data =", data_bool, "type =", type(data_bool))

