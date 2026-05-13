kata = input("Masukkan kata: ")
hasil = ""

for i in range(len(kata)-1, -1, -1):
    hasil += kata[i]

print("Hasil dibalik:", hasil)