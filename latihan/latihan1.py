# tampilkan output dengan kata "Hello Word" dan nama kalian serta tampilkan hasilnya
# Contoh
print("Hello World")
print("Nama saya James Riandi")

# tampilkan nama, npm, kelas, dan IPK menggunakan variabel serta tampilkan hasilnya
# Contoh
nama_saya = "James Riandi"
npm_saya = 55419947
kelas_saya = "4IA20"
ipk_saya = 3.60

print(
    "Hello, nama saya",
    nama_saya,
    ", NPM saya adalah",
    npm_saya,
    ", kelas saya adalah",
    kelas_saya,
    ", dan IPK saya adalah %0.2f" % ipk_saya,
)

"""buatlah program dengan menginputkan nama, npm, kelas, dan IPK menggunakan variabel 
serta tampilkan hasilnya"""
# Contoh
nama = input("Masukan nama saya: ")
npm = int(input("Masukan NPM anda: "))
kelas = input("Masukan kelas anda: ")
ipk = float(input("Masukan IPK anda: "))

print(
    "Hello, nama saya",
    nama,
    ", NPM saya adalah",
    npm,
    ", kelas saya adalah",
    kelas,
    ", dan IPK saya adalah %0.2f" % ipk,
)
