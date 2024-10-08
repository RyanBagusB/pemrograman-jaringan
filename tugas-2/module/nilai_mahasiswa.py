def hitung_nilai_akhir(tugas, kuis, uts, uas):
    return (tugas * 0.2) + (kuis * 0.2) + (uts * 0.3) + (uas * 0.3)

def nilai_huruf(nilai_akhir):
    if nilai_akhir >= 88:
        return 'A'
    elif nilai_akhir >= 77:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 45:
        return 'D'
    else:
        return 'E'
