# Mendefinisikan dua matriks 2x2 sebagai contoh
matriks1 = [[1, 2], [3, 4]]
matriks2 = [[5, 6], [7, 8]]

# Menambahkan kedua matriks
result = [[matriks1[i][j] + matriks2[i][j] for j in range(len(matriks1[0]))] for i in range(len(matriks1))]

print("Hasil penjumlahan matriks:")
for r in result:
    print(r)
