total = 0

harga = int(input("Masukkan harga barang: "))

while harga <= 0:
    total = total + harga
    harga = int(input("Masukkan harga barang: "))

if total >= 50000:
    total = total - 5000

print("Total yang harus dibayar =", total)