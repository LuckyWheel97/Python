

a = 10
b =3

# opersi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi kali *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi bagi /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi pangkat **
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi
# operasi yang berada dalam tanda kurung () akan di eksekusi terlebih dahulu
# operasi perkalian * dan pembagian / akan di eksekusi setelah operasi dalam tanda kurung () dan sebelum operasi penjumlahan + dan pengurangan -
# operasi penjumlahan + dan pengurangan - akan di eksekusi setelah operasi dalam tanda kurung () dan operasi perkalian * dan pembagian /
# operasi yang memiliki prioritas yang sama akan di eksekusi dari kiri ke kanan

x = 10
y = 3
z = 2
hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)