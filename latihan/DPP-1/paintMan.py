print("Selamat Datang di PaintMan V1.0")

jumlah_dinding = int(input("Jumlah dinding: "))

luas_total = 0

for i in range(jumlah_dinding):
    print("~~")
    print("Dinding", i + 1)
    panjang = float(input("Panjang dinding (m): "))
    lebar = float(input("Lebar dinding (m): "))
    luas_dinding = panjang * lebar
    print("Luas dinding: %0.2f" % luas_dinding)
    luas_total += luas_dinding

print("~~")
print("Luas total dari semua dinding adalah", luas_total)
