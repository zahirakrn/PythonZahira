#Program Larik Angka
#I.S.: elemen array angka yang di berikan harga awal
#F.S.: menampilkan elemen array angka dalam bentuk tabel
import os

#kostanta
MAKSANGKA = 10

#subrutin menu pilihan 
def MenuPilihan(Menu):
    print('\033[34m<<--MENU PILIHAN-->>\033[30m')
    print('--------------------')
    print('1. Isi Elemen Larik')
    print('2. Tambah Elemen Larik')
    print('3. Sisip Elemen Larik')
    print('4. Hapus Elemen Larik')
    print('5. Tampil Elemen Larik')
    print('0. Keluar Menu')
    Menu = int(input('Pilihan Anda? '))
    return Menu


#subrutin mengisi elemen array angka
def IsiAngka(Angka,BanyakData):
    BanyakData = int(input('Banyak data yang di olah = '))
    os.system('cls')
    print(f'\033[33m<<PENGISIAN {BanyakData} ELEMEN LARIK ANGKA>>\033[30m')
    for i in range(BanyakData):
        Angka[i] = int(input('Angka Ke-{} = '.format(i+1)))
    
    return BanyakData

#subrutin menambahkan satu elemen di belakang
def TambahAngka(Angka,BanyakData,AngkaBaru):
    Angka[BanyakData] = AngkaBaru

#subrutin menyisipkan satu elemen di posisi tertentu
def SisipAngka(Angka,BanyakData,PosisiSisip,AngKaBaru):
    for i in range(BanyakData-1,PosisiSisip-1,-1):
        Angka [i+1] = Angka [i]

    Angka[PosisiSisip] = AngkaBaru

#subrutin menghapus satu elemen di posisi tertentu
def HapusAngka(Angka,BanyakData,PosisiHapus):
    for i in range(PosisiHapus+1,BanyakData):
        Angka [i-1] = Angka [i]

    Angka[BanyakData-1] = 0

#subrutin menampilkan elemen array angka
def TampilAngka(Angka,BanyakData):
    os.system('cls')
    print('  \033[32mISI LARIK ANGKA\033[30m')
    print('---------------------')
    print('| No | Elemen larik |')
    print('=====================')
    for i in range(BanyakData):
        print(f'| {i+1:2} |     {Angka[i]:4}     |')
    print('----------------------')

#badan program utama
os.system('cls')
#penciptaan array Angka
Angka =[0] * MAKSANGKA
TampilAngka(Angka,MAKSANGKA)
print()
os.system('pause')
os.system('cls')
Menu = 0
Menu = MenuPilihan(Menu)
BanyakData = 0
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1:
            print('\033[33m<<PENGISIAN ELEMEN LARIK ANGKA>>\033[30m')
            BanyakData = IsiAngka(Angka,BanyakData)
            TampilAngka(Angka,BanyakData)
        case 2:
            if(BanyakData > 0):
                if (BanyakData < MAKSANGKA):
                    print('\033[33m<<PENAMBAHAN ELEMEN LARIK ANGKA>>\033[30m')  
                    AngkaBaru =int(input('Angka yang akan di Tambahkan = '))
                    TambahAngka(Angka,BanyakData,AngkaBaru)
                    BanyakData +=1
                    TampilAngka(Angka,BanyakData)
                else:
                    print('\033[31mData sudah penuh\033[30m')
            else:
                print('\033[31mPilih Menu No.1 Terlebih Dahulu!\033[30m')
        case 3:
            if(BanyakData > 0):
                if (BanyakData < MAKSANGKA):
                    print('\033[33m<<PENYISIPAN ELEMEN LARIK ANGKA>>\033[30m')  
                    AngkaBaru =int(input('Angka yang akan di sisipkan = '))
                    PosisiSisip = int(input('{} disisipan pada posisi ke = '.format(AngkaBaru)))
                    PosisiSisip -= 1
                    if (PosisiSisip >= 0) and (PosisiSisip<= BanyakData - 1):
                        SisipAngka(Angka,BanyakData,PosisiSisip,AngkaBaru)
                        BanyakData +=1
                        TampilAngka(Angka,BanyakData)
                    else:
                        print(f'Posisi ke-{PosisiSisip+1} Tidak Ada!')
                else:
                    print('\033[31mData sudah penuh\033[30m') 
            else:
                print('\033[31mPilih Menu No.1 Terlebih Dahulu!\033[30m')
        case 4:
            if(BanyakData > 0):
                print('\033[33m<<PENGHAPUSAN ELEMEN LARIK ANGKA>>\033[30m')
                PosisiHapus = int(input('Angka Yang di hapus pada posisi ke = '))
                PosisiHapus -= 1
                if (PosisiHapus >= 0) and (PosisiHapus<= BanyakData - 1):
                    HapusAngka(Angka,BanyakData,PosisiHapus)
                    BanyakData -=1
                    if (BanyakData > 0):
                        TampilAngka(Angka,BanyakData)
                    else:
                        print('Data Sudah Kosong')
                else:
                    print(f'Posisi ke-{PosisiHapus+1} Tidak Ada!')
            else:
                print('\033[31mPilih Menu No.1 Terlebih Dahulu!\033[30m')
        case 5:
            if(BanyakData > 0):
               TampilAngka(Angka,BanyakData)
            else:
                print('\033[31mData Masih Kosong!\033[30m')
        case _:
                print('\033[31mNomor Menu Tidak Ada!\033[30m')
    print()
    os.system('pause')
    os.system('cls')
    Menu = MenuPilihan(Menu)