## latihan konversi satuan temperature

# program konversi celcius ke satuan lain
# celcius
print("====Program Konversi Temperature====")
celcius = float(input("Masukan suhu dalam celcius: "))
# fahrenheit
fahrenheit = (celcius * (9/5)) + 32
print(celcius, "celcius =", fahrenheit, "fahrenheit")
# reamur
reamur = celcius * (4/5)
print(celcius, "celcius =", reamur, "reamur")
# kelvin
kelvin = celcius + 273.15
print(celcius, "celcius =", kelvin, "kelvin")
0

# tugas
# konversi fahrenheit ke kelvin
celcius = (fahrenheit - 32) * (5/9)
kelvin = celcius + 273.15
print(fahrenheit, "fahrenheit =", kelvin, "kelvin")

# kelvin ke fahrenheit
celcius = kelvin - 273.15
fahrenheit = (celcius * (9/5)) + 32
print(kelvin, "kelvin =", fahrenheit, "fahrenheit")


