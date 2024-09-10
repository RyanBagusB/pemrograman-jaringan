from module.hitung_total import hitung_total_pembelian

daftar_belanja = []

while True:
    nama_barang = input("Nama Barang: ")
    harga = int(input("Harga: "))
    jumlah = int(input("Jumlah: "))
    
    daftar_belanja.append({
        'nama': nama_barang,
        'harga': harga,
        'jumlah': jumlah
    })
    
    lagi = input("Tambah barang lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

total_pembelian = hitung_total_pembelian(daftar_belanja)

# Header tabel
print(f"{'Nama':<15} {'Jumlah':<10} {'Harga':<10} {'Sub Harga':<10}")

# Isi tabel
for barang in daftar_belanja:
    sub_harga = barang['harga'] * barang['jumlah']
    print(f"{barang['nama']:<15} {barang['jumlah']:<10} {barang['harga']:<10} {sub_harga:<10}")

# Total pembelian
print(f"{'Total pembelian:'} {total_pembelian}")
