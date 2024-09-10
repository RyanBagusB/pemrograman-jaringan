from module.konversi_nilai import nilai_angka_ke_huruf

nilai = int(input("Masukkan nilai angka: "))
nilai_huruf = nilai_angka_ke_huruf(nilai)
print(f"Nilai huruf: {nilai_huruf}")
