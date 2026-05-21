#Contoh WHILE Sistem pengisian baterai laptop
#yang akan terus berjalan selama daya mencapai 100%
daya = 0
while daya < 1000:
  print("Mengisi daya------ posisi:",daya, "%")
  daya += 50 #Menambahkan daya setiap putaran
 
print("Baterai Penuh") no