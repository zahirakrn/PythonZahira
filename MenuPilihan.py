#Program Menu Pilihan
#I.S. : pengguna memilih salah satu nomor menu(PilihMenu)
#F.S. : menampilkan hasil sesuai nomor menu yang dipilih
import os

#badan program
#menampilkan menu pilihan
os.system('cls')
print('MENU PILIHAN')
print('------------')
print('1. Suku ke-N dari Deret Fibonacci')
print('2. S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
print('0. Keluar')
#validasi menu pilihan
PilihMenu = int(input('Pilihan Anda? '))
#validasi menu pilihan
while (PilihMenu < 0) or (PilihMenu >2) :
    print('\033[031mNomor Menu Hanya 0/1/2..Ulangi!\033{0m')
    os.system('pause')
    os.system('cls')
    print('MENU PILIHAN')
    print('------------')
    print('1. Suku ke-N dari Deret Fibonacci')
    print('2. S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
    print('0. Keluar')
    PilihMenu = int(input('Pilihan Anda? '))

#memproses sesuai nomor menu yang dipilih
while (PilihMenu != 0):
    os.system('cls')
    #menegecek nomor menu yang dipilih
    match(PilihMenu):
        case 1:
            print('<<PROGRAM SUKU KE-N DARI FIBONACCI>>')
            #memasukkan suku(N) yang diinginkan
            N = int(input('Suku Ke- = '))
            #validasi suku(N)
            while (N < 1):
                print('\033[031mNomor Menu Hanya 0/1/2..Ulangi!\033{0m')
                os.system('pause')

                os.system('cls')
                print('<<PROGRAM SUKU KE-N DARI DERET FIBONACCI>>')
                #memasukan suku(N) yang diinginkan
                N = int(input('Suku Ke- = '))
            #menentukan suku ke-N dari deret fibonacci
            if (N == 1) or (N == 2):
                Fibo = 1
            else :
                SukuN1 = 1
                SukuN2 = 1
                for i in range(2,N):
                    Fibo = SukuN1 + SukuN2
                    SukuN1 = SukuN2
                    SukuN2 = Fibo

            #menampilkan suku ke-N dari deret fibonacci
            print(f'suku ke-(N) dari deret Fibonacci adalah {Fibo}')
        case 2:
            print('<<PROGRAM MENGHITUNG S = 2/3 - 5/7 + 16/21 - 65/81 + ..>>')
            #memasukkan banyaknya suku yang dihitung
            BanyakSuku = int(input('Banyak Suku = '))
            #validasi banyak suku
            while (BanyakSuku < 1) or (BanyakSuku > 10):
                print('\033[031mBanyak suku hanya diantara 1-10..Ulangi!\033{0m')
                os.system('pause')
                os.system('cls')
                print('<<PROGRAM MENGHITUNG S = 2/3 - 5/7 + 16/21 - 65/81 + ..>>')
                #memasukan suku(N) yang akan dihitung kembali
                BanyakSuku = int(input('Banyak Suku = '))
            # #menghitung S = 2/3 - 5/7 + 16/21 - 65/81 + ..
            S = 0
            Pembilang = 1
            print(f'S = ',end="")
            for i in range(BanyakSuku):
                i += 1 #i = i + 1
                temp = Pembilang
                Pembilang = Pembilang * i + 1
                Penyebut = Pembilang + temp
                #S = S - (-1)**i * (Pembilang/Penyebut)
                if (i == 1):
                    S = S + Pembilang/Penyebut
                    print(f'{Pembilang}/{Penyebut}',end='')
                elif (i % 2 == 0):
                    S = S - Pembilang/Penyebut
                    print(f' - {Pembilang}/{Penyebut}',end='')
                else:
                    S = S + Pembilang/Penyebut
                    print(f' + {Pembilang}/{Penyebut}',end='')

            print()
            print('  = ',end='')
            #menampilkan harga S
            print(f'{S:.3f}')

    os.system('pause')
    #menampilkan menu pilihan
    os.system('cls')
    print('MENU PILIHAN')
    print('------------')
    print('1. Suku ke-N dari Deret Fibonacci')
    print('2. S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
    print('0. Keluar')
    #validasi menu pilihan
    PilihMenu = int(input('Pilihan Anda? '))
    #validasi menu pilihan
    while (PilihMenu < 0) or (PilihMenu >2) :
        print('\033[031mNomor Menu Hanya 0/1/2..Ulangi!\033{0m')
        os.system('pause')
        os.system('cls')
        print('MENU PILIHAN')
        print('------------')
        print('1. Suku ke-N dari Deret Fibonacci')
        print('2. S = 2/3 - 5/7 + 16/21 - 65/81 + ..')
        print('0. Keluar')
        PilihMenu = int(input('Pilihan Anda? '))