# Latihan1
nama = input("Masukan nama anda: ")
npm = input("Masukan NPM anda: ")
kelas = input("Masukan kelas anda: ")
nilai_uts = float(input("Masukan nilai UTS anda: "))
nilai_uas = float(input("Masukan nilai UTS anda: "))
total_nilai = nilai_uts + nilai_uas
rata_nilai = total_nilai / 2

# Menentukan Grade Nilai
if rata_nilai > 100:
    print("Nilai rata - rata melebihi angka 100")
elif rata_nilai >= 90:
    print("Nilai Rata - rata anda adalah:", rata_nilai)
    print("Grade A")
elif rata_nilai >= 70:
    print("Nilai Rata - rata anda adalah:", rata_nilai)
    print("Grade B")
elif rata_nilai >= 50:
    print("Nilai Rata - rata anda adalah:", rata_nilai)
    print("Grade C")
elif rata_nilai >= 30:
    print("Nilai Rata - rata anda adalah:", rata_nilai)
    print("Grade D")
elif rata_nilai >= 0:
    print("Nilai Rata - rata anda adalah:", rata_nilai)
    print("Grade E")
else:
    print("Tidak ada nilai minus")
