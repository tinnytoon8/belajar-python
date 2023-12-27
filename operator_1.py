# Operator Aritmatika
# + , -, *, /, %, **, //

# Contoh 1
x = 5
y = 2
print("Penjumlahan =", x + y)
print("Pengurangan =", x - y)
print("Perkalian =", x * y)
print("Pembagian =", x / y)
print("Modulus/Sisa Bagi =", x % y)
print("Pangkat =", x**y)
print("Pembagian Bulat =", x // y)

# Contoh 2
hitung1 = 1 + 1 * 0
print(hitung1)

# Python sudah mengenal PEMDAS
# PEMDAS(Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right))

hitung2 = 1 * 1 + 90 / 3
print(hitung2)

hitung3 = (1 * 1) + (90 / 3)
print(hitung3)
# Atas dan bawah sama saja

# Operator Perbandingan
# <, >, <=, =>, ==, !=
angka1 = 3
angka2 = 6
print(angka1 < angka2)  # Nilai True
print(angka1 > angka2)  # Nilai False
print(angka1 == angka2)  # Nilai False

angka3 = 3
angka4 = 6
print(angka1 >= angka3)  # Nilai True
print(angka1 <= angka3)  # Nilai True
print(angka2 <= angka4)  # Nilai True
print(angka1 == angka3)  # Nilai True
print(angka3 != angka4)  # Nilai True

# Operator Penugasan
# Menyatakan suatu perintah atau fungsi perhitungan dalam bentuk yang disingkat
# +=, -=, *=, /=, %=, **=, //=

a = 1  # sama dengan
a *= 5  # sama aja dengan a = a * 5
print(a)

b = 3
c = 4
b += c  # sama aja dengan b = b + b
print(b)

# Operator Logika / Boolean
# AND, OR, dan Not
boolean1 = True
boolean2 = False
hasil1 = boolean1 and boolean2
print(hasil1)
hasil2 = boolean1 and boolean1
print(hasil2)
hasil3 = boolean1 or boolean2
print(hasil3)
hasil4 = boolean2 or boolean2
print(hasil4)
hasil5 = boolean2 and boolean2
print(hasil5)
