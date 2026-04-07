#Program Penentuan Toko Termurah
#I.S. : pengguna memasukkan data pelanggan, data bahan baku, data toko, 
#       data kebutuhan bahan baku perpelanggan dan data harga bahan baku 
#       per toko
#F.S. : menampilkan toko termurah untuk per pelanggan

import os

#konstanta
MAKSPELANGGAN = 6
MAKSBAHAN = 5
MAKSTOKO = 3

#subrutin memasukkan semua data yang digunakan
def IsiData(P,B,T,Kebutuhan,Harga):
    os.system('cls')
    print(f'<<PENGISIAN DATA PELANGGAN SEBANYAK {MAKSPELANGGAN} DATA>>')
    for i in range(MAKSPELANGGAN):
        P[i] = str(input('Nama Pelanggan Ke-{} : '.format(i+1)))

    print()
    print(f'<<PENGISIAN DATA BAHAN BAKU SEBANYAK {MAKSBAHAN} DATA>>')
    for j in range(MAKSBAHAN):
        B[j] = str(input('Bahan Baku Ke-{} : '.format(j+1)))

    print()
    print(f'<<PENGISIAN DATA KEBUTUHAN BAHAN BAKU PER PELANGGAN>>')
    for i in range(MAKSPELANGGAN):
        print(f'Kebutuhan Pelanggan {P[i]}')
        for j in range(MAKSBAHAN):
            Kebutuhan[i][j] = int(input('Jumlah Bahan Baku {} : '.format(B[j])))

        print()

    print(f'<<PENGISIAN DATA TOKO SEBANYAK {MAKSTOKO} DATA>>')
    for k in range(MAKSTOKO):
        T[k] = str(input('Nama Toko Ke-{} : '.format(k+1)))

    print()
    print(f'<<PENGISIAN DATA HARGA BAHAN BAKU PER TOKO>>')
    for j in range(MAKSBAHAN):
        print(f'Harga Bahan Baku {B[j]}')
        for k in range(MAKSTOKO):
            Harga[j][k] = int(input('Harga di Toko {} : Rp. '.format(T[k])))

        print()

#subrutin menghitung kebutuhan dengan harga (TotalHarga)
def TotalHarga(Kebutuhan,Harga,Hasil):
    print('<<PERHITUNGAN TOTAL HARGA PER PELANGGAN PER TOKO>>')
    for i in range(MAKSPELANGGAN):
        print(f'Total Harga Pelanggan {P[i]}')
        for k in range(MAKSTOKO):
            Hasil[i][k] = 0
            for j in range(MAKSBAHAN):
                Hasil[i][k] = Hasil[i][k] + Kebutuhan[i][j] * Harga[j][k]

            print(f'Total Harga di Toko {T[k]} = Rp. {Hasil[i][k]:,}')

        print() 

#subrutin menentukan total harga termurah
def Termurah(Hasil,Murah):
    print(f'<<PENENTUAN TOTAL HARGA TERMURAH PER PELANGGAN>>')
    for i in range(MAKSPELANGGAN):
        Min = Hasil[i][0]
        Murah[i] = 0
        for k in range(1,MAKSTOKO): 
            if (Hasil[i][k] < Min):
                Min = Hasil[i][k]
                Murah[i] = k

        print(f'Total Harga Termurah Untuk {P[i]} : Rp. {Min:,}')  

#subrutin menampilkan toko termurah per pelanggan
def TampilTokoTermurah(Murah):
    print()
    print('<<REKOMENDASI TOKO TERMURAH PER PELANGGAN>>')
    for i in range(MAKSPELANGGAN):
        print(f'Pelanggan {P[i]} direkomendasikan ke ',end='')  
        if (Murah[i] == 0):
            print('Toko 1')
        elif (Murah[i] == 1):
            print('Toko 2') 
        else:
            print('Toko 3')     

#badan program utama
#penciptaan data pelanggan (P)
P = ['/'] * MAKSPELANGGAN

#penciptaan data bahan baku (B)
B = ['/'] * MAKSBAHAN

#penciptaan data kebutuhan bahan baku
Kebutuhan = [0] * MAKSPELANGGAN
for j in range(MAKSPELANGGAN):
    Kebutuhan[j] = [0] * MAKSBAHAN

#penciptaan data toko (T)
T = ['/'] * MAKSTOKO

#penciptaan data harga bahan baku per toko
Harga = [0] * MAKSBAHAN
for k in range(MAKSBAHAN):
    Harga[k] = [0] * MAKSTOKO

#penciptaan data hasil perkalian matriks (Hasil)
Hasil = [0] * MAKSPELANGGAN
for k in range(MAKSPELANGGAN):
    Hasil[k] = [0] * MAKSTOKO

#penciptaan data termurah (Murah)
Murah = [0] * MAKSPELANGGAN

#memanggil subrutin memasukkan semua data yang digunakan
IsiData(P,B,T,Kebutuhan,Harga)

#memanggil subrutin menghitung total harga (perkalian matriks Kebutuhan dengan matriks Harga)
TotalHarga(Kebutuhan,Harga,Hasil)

#memanggil subrutin total harga termurah
Termurah(Hasil,Murah)

#memanggil subrutin menampilkan toko termurah
TampilTokoTermurah(Murah)