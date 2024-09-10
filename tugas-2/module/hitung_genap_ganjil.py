def hitung_genap_ganjil(bilangan):
    genap = [x for x in bilangan if x % 2 == 0]
    ganjil = [x for x in bilangan if x % 2 != 0]
    return genap, ganjil
