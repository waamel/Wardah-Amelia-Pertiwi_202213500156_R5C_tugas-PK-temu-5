# Program menghitung IPS mahasiswa

# Input jumlah mata kuliah
jml_mk = int(input("Berapa jumlah mata kuliah? "))

# Inisialisasi variabel total nilai
total_nilai = 0

# Perulangan untuk input nilai setiap mata kuliah
for i in range(1, jml_mk + 1):
  nilai_mk = input(f"Nilai MK {i}: ").upper()

  # Percabangan untuk konversi nilai ke angka
  if nilai_mk == 'A':
    nilai_angka = 4
  elif nilai_mk == 'B':
    nilai_angka = 3
  elif nilai_mk == 'C':
    nilai_angka = 2
  elif nilai_mk == 'D':
    nilai_angka = 1
  else:
    print("Nilai tidak valid!")
    break

  # Menambahkan nilai angka ke total nilai
  total_nilai += nilai_angka

# Menghitung IPS
ips = total_nilai / jml_mk

# Menampilkan hasil IPS
print(f"Nilai IPS anda semester ini: {ips:.2f}")