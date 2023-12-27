# Program Konversi Suhu
print("===== Konversi Suhu =====")
print("|1. Celcius             |")
print("|2. Reamur              |")
print("|3. Fahrenheit          |")
print("|4. Kelvin              |")
print("=========================")
pil = int(input("Masukan pilihan anda: "))

if pil == 1:
    celcius = float(input("Masukan suhu dalam Celcius: "))
    hitung_cr = 4 / 5 * celcius
    hitung_cf = 9 / 5 * celcius + 32
    hitung_ck = celcius + 273

    print("Suhu dalam Reamur:", hitung_cr)
    print("Suhu dalam Fahrenheit:", hitung_cf)
    print("Suhu dalam Kelvin:", hitung_ck)
elif pil == 2:
    reamur = float(input("Masukan suhu dalam Reamur: "))
    hitung_rc = 5 / 4 * reamur
    hitung_rf = 9 / 4 * reamur + 32
    hitung_rk = hitung_rc + 273

    print("Suhu dalam Celcius:", hitung_rc)
    print("Suhu dalam Fahrenheit:", hitung_rf)
    print("Suhu dalam Kelvin:", hitung_rk)
elif pil == 3:
    fahrenheit = float(input("Masukan suhu dalam Fahrenheit: "))
    hitung_fc = 5 / 9 * fahrenheit * (fahrenheit - 32)
    hitung_fr = 4 / 9 * fahrenheit * (fahrenheit - 32)
    hitung_fk = hitung_fc + 273

    print("Suhu dalam Celcius:", hitung_fc)
    print("Suhu dalam Reamur:", hitung_fr)
    print("Suhu dalam Kelvin:", hitung_fk)
elif pil == 4:
    kelvin = float(input("Masukan suhu dalam Kelvin: "))
    hitung_kc = kelvin - 273
    hitung_kr = 4 / 5 * hitung_kc
    hitung_kf = 9 / 5 * hitung_kc + 32

    print("Suhu dalam Celcius:", hitung_kc)
    print("Suhu dalam Reamur:", hitung_kr)
    print("Suhu dalam Fahrenheit:", hitung_kf)
else:
    print("Pilihan anda tidak ada!")
