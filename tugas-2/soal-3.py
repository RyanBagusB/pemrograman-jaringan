from module.hitung_genap_ganjil import hitung_genap_ganjil

jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))
bilangan = []

for i in range(jumlah_bilangan):
    angka = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(angka)

genap, ganjil = hitung_genap_ganjil(bilangan)

print(f"Jumlah bilangan genap: {len(genap)} yaitu {' '.join(map(str, genap))}")
print(f"Jumlah bilangan ganjil: {len(ganjil)} yaitu {' '.join(map(str, ganjil))}")
