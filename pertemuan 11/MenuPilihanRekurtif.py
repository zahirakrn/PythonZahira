#Program Menu Pilihan Rekurtif
#I.S. : pengguna memilih salah satu nomor menu
#F.S. : menampilkan hasil sesuai nomor menu yang dipilih
import os

#subrutin menampilkan menu pilihan
def MenuPilihan(Pilih):
        print('\033[33m<<--MENU PILIHAN-->>\033[30m')
        print('--------------------')
        print('1. Faktorial')
        print('2. Barisan 1,6,4,11,9,16,16...')
        print('0. Keluar')
        Pilih = int(input('Pilihan Anda? '))
        return Pilih

#subrutin memasukan harga yang di faktortialkan (n)
def IsiN(N):
    N = int(input('Harga Yang Difaktorialkan (N) = '))
    #validasi
    while (N < 0):
        print('\033[31mHarga Yang Difaktorialkan (N) Tidak Boleh Negatif!\033[30m')
        print()
        os.system('pause')
        os.system('cls')
        print('\033[34m-->PROGRAM HITUNG FAKTORIAL<--\033[30m')
        N = int(input('Harga Yang Difaktorialkan (N) = '))

    return N
#subsitusi menghitunag faktorial secara rekurtif
def Faktorial(N):
    if (N == 0) or (N == 1):
        return 1
    else:
        return N * Faktorial(N - 1)

#subrutuin menampilkan hasil faktorial dari N
def TampilFaktorial(N):
    print(f'{N:2}! = ' , end = ' ')
    if (N> 1):
        for i in range(N,0,-1):
            print(f'\033[32m{i}',end='')
            if(i>1):
                print('\033[30m x ',end='')

        print()
        print('\033[30m    = ',end='') 

    print(f'\033[32m{Faktorial(N)}\033[30m')

#subrutin memasukan banyak susku (NSuku)
def IsiBanyakSuku(NSuku):
    NSuku = int(input('Banyak Suku = '))
    #validasi
    while (NSuku < 1) or (NSuku > 50):
        print('\033[31mBanyak Suku Hanya Antara 1 Sampai 50!\033[30m')
        print()
        os.system('pause')
        os.system('cls')
        print('\033[34m-->PROGRAM BARISAN 1,6,4,11,9,16,16...<--\033[30m')
        NSuku = int(input('Banyak Suku = '))

    return NSuku
#subrutin menghitung per suku barisan 1,6,4,11,9,16,16...
def SukuN(NSuku):
    if (NSuku == 1):
        return 1
    elif (NSuku == 2):
        return 6
    else:
        if (NSuku % 2 == 1):
            return SukuN(NSuku - 2) + NSuku
        else:
            return SukuN(NSuku - 2) + 5
        
#subrutin menampilkan barisan 1,6,4,11,9,16,16...
def TampilBarisan(NSuku):
    os.system('cls')
    print('\033[34m-->PROGRAM BARISAN 1,6,4,11,9,16,16...<--\033[30m')
    print(f'Barisan Kombinasi Sebanyak \033[31m{NSuku}\033[32m Suku Adalah')
    for i in range(1,NSuku+1):
        print(f' {SukuN(i)}',end='')
        if (i < NSuku):
            print(', ',end='')
        
    print()
#badan program utama
os.system('cls')
Pilih = 0
Pilih = MenuPilihan(Pilih)
while (Pilih != 0):
    os.system('cls')
    match(Pilih):
        case 1:
            print('\033[34m-->PROGRAM HITUNG FAKTORIAL<--\033[30m')
            N = 0
            N = IsiN(N)
            TampilFaktorial(N)
            print()
        case 2:
            print('\033[34m-->PROGRAM BARISAN 1,6,3,11,9,16,16...<--\033[30m')
            NSuku = 0
            NSuku = IsiBanyakSuku(NSuku)
            TampilBarisan(NSuku)
            print()
        case _:
            print('\033[31m-->NOMOR MENU TIDAK ADA!<--\033[30m')
           
            print()

    os.system('pause')
    os.system('cls')
    Pilih = MenuPilihan(Pilih)
