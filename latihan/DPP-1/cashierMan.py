total_payment = 0

customer_name = input("Customer Name: ")

billName = f"{customer_name}.txt"
bill = open(f"{customer_name}.txt", "w")

print("=" * 74, file=bill)
print(f"{'COLDBREW CAFE BILL':^74}", file=bill)
print("=" * 74, file=bill)

while True:
    product_name = input("Product (Enter to finish): ")

    if product_name == "":
        break

    quantity = int(input("Quantity: "))
    price = int(input("Price: "))
    total_price = quantity * price
    total_payment += total_price

    print(
        f"{quantity:4d} | {product_name:25s} | Rp{price:10.2f} | Rp{total_price:15.2f}\n",
        file=bill,
    )

print("=" * 74, file=bill)
print(f"\nTotal Payment: Rp{total_payment:,.2f}\n", file=bill)
print(f"\nTotal Payment: Rp{total_payment:,.2f}\n")

print(f"Billing data has been saved to {billName}")
