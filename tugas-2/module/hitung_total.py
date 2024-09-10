# hitung_total.py

def hitung_total_pembelian(daftar_belanja):
    total = 0
    for barang in daftar_belanja:
        total += barang['harga'] * barang['jumlah']
    return total
