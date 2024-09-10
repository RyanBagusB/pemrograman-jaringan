def hitung_rata_rata(data):
    return sum(data) / len(data)

def hitung_median(data):
    data.sort()
    n = len(data)
    tengah = n // 2
    if n % 2 == 0:
        return (data[tengah - 1] + data[tengah]) / 2
    else:
        return data[tengah]

def hitung_modus(data):
    frekuensi = {}
    for angka in data:
        if angka in frekuensi:
            frekuensi[angka] += 1
        else:
            frekuensi[angka] = 1
    
    modus = max(frekuensi, key=frekuensi.get)
    nilai_tertinggi = frekuensi[modus]

    modus_list = [k for k, v in frekuensi.items() if v == nilai_tertinggi]
    
    if len(modus_list) > 1:
        return modus_list
    return modus

# Menghitung rata-rata dari 3 bilangan bulat sembarang.
data = [3, 6, 5]
rata_rata = hitung_rata_rata(data)
print("Rata-rata:", rata_rata)

# Buatlah program memasukkan 10 data, hitung rata2, median, dan modus
data = []
for i in range(10):
    angka = int(input(f"Masukkan data ke-{i+1}: "))
    data.append(angka)

median = hitung_median(data)
modus = hitung_modus(data)
rata_rata = hitung_rata_rata(data)

print("Rata-rata:", rata_rata)
print("Median:", median)
print("Modus:", modus)
