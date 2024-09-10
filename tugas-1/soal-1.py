nilai = float(input("Masukkan nilai: "))

if nilai >= 88:
    print("Kriteria A")
elif 77 <= nilai < 88:
    print("Kriteria B")
elif 60 <= nilai < 77:
    print("Kriteria C")
elif 45 <= nilai < 60:
    print("Kriteria D")
else:
    print("Kriteria E")
