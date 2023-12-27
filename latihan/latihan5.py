saldo_awal = 50000
deposit = int(input("Mau deposit berapa: "))
saldo_total = saldo_awal + deposit
hutang = 100000

if saldo_total >= hutang:
    print("Total saldo anda yaitu", saldo_total)
    print("Anda bisa bayar hutang")
else:
    print("Total saldo anda yaitu", saldo_total)
    print("Anda belum bisa bayar hutang")
