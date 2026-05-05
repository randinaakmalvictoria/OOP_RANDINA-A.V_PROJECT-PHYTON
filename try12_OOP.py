# CONTOH STRUKTUR PENCABANGAN IF
# Input data dari pengguna
nilai_ujian = float(input("Masukan Nilai Ujian Siswa: "))


# struktur kontrol percabangan majemuk
if nilai_ujian >=90:
   predikat= "Sangat Baik (A)"
elif nilai_ujian >=75:
   predikat= "Baik (B)"
elif nilai_ujian >=60:
  predikat= "Cukup (C)"
else:
  predikat="Kurang (D)-Memelukan Remedial"

# menampilkan hasil keputusan 
print ("Hasil Evaluasi:", predikat)