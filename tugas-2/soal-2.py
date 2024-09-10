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

for barang in daftar_belanja:
    sub_harga = barang['harga'] * barang['jumlah']
    print(f"{barang['nama']} {barang['jumlah']} {sub_harga}")

print(f"Total pembelian: {total_pembelian}")
