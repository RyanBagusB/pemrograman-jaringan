from module.nilai_mahasiswa import hitung_nilai_akhir, nilai_huruf
import matplotlib.pyplot as plt

mahasiswa = []

for i in range(5):
    nama = input(f"Nama Mhs {i+1}: ")
    tugas = int(input("N.Tugas: "))
    kuis = int(input("N.Kuis: "))
    uts = int(input("N.UTS: "))
    uas = int(input("N.UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, kuis, uts, uas)
    huruf = nilai_huruf(nilai_akhir)
    
    mahasiswa.append({
        'nama': nama,
        'nilai_akhir': nilai_akhir,
        'nilai_huruf': huruf
    })

print("------------------------------------------------------------------------------------------")
print(f"{'No.':<3} {'Nama Mhs':<10} {'N.Tugas':<8} {'N.Kuis':<7} {'N.UTS':<6} {'N.UAS':<6} {'Nilai Akhir':<12} {'Nilai Huruf':<10}")
print("------------------------------------------------------------------------------------------")

jumlah_A = jumlah_B = jumlah_C = jumlah_D = jumlah_E = 0

for i, mhs in enumerate(mahasiswa, start=1):
    print(f"{i:<3} {mhs['nama']:<10} {tugas:<8} {kuis:<7} {uts:<6} {uas:<6} {mhs['nilai_akhir']:<12.2f} {mhs['nilai_huruf']:<10}")
    
    if mhs['nilai_huruf'] == 'A':
        jumlah_A += 1
    elif mhs['nilai_huruf'] == 'B':
        jumlah_B += 1
    elif mhs['nilai_huruf'] == 'C':
        jumlah_C += 1
    elif mhs['nilai_huruf'] == 'D':
        jumlah_D += 1
    elif mhs['nilai_huruf'] == 'E':
        jumlah_E += 1

print("------------------------------------------------------------------------------------------")
print(f"Jumlah A: {jumlah_A}")
print(f"Jumlah B: {jumlah_B}")
print(f"Jumlah C: {jumlah_C}")
print(f"Jumlah D: {jumlah_D}")
print(f"Jumlah E: {jumlah_E}")

nilai_huruf_counts = [jumlah_A, jumlah_B, jumlah_C, jumlah_D, jumlah_E]
huruf_labels = ['A', 'B', 'C', 'D', 'E']

plt.bar(huruf_labels, nilai_huruf_counts)
plt.xlabel('Nilai Huruf')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Distribusi Nilai Huruf Mahasiswa')
plt.show()
