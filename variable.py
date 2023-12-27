# variabel -> tempat menyimpan data sementara
# konstanta -> tempat menyimpan data tetap
# String -> tipe data gabungan dari banyak karakter
# Integer -> tipe data bilangan bulat

x = 1
print(x)

nama_saya = "Budi Kusuma"
print(nama_saya)
print("Hello, nama saya " + nama_saya)
print("Hello, nama saya", nama_saya)

umur_saya = 12
print(umur_saya)
print("Umur saya yaitu", umur_saya, "tahun")
print("Umur saya yaitu " + str(umur_saya) + " tahun")

# Menggunakan format String
print(f"Hello, nama saya {nama_saya} dan umur saya adalah {umur_saya} tahun")

# Menggunakan metode format()
print(
    "Hello, nama saya {}".format(nama_saya)
    + " dan umur saya adalah {}".format(umur_saya)
    + " tahun"
)
