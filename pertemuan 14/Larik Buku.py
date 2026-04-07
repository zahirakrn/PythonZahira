#Program Penggolahan Larik Buku 
#I.S. pengguna memasukan bulan, tahun dan larik buku
#F.S. menampilkan daftar buku dalam bentuk tabel
import os

#konstanta
MAKSBUKU = 50

#subrutin menu pilihan
def MenuPilihan(Menu):
    os.system('cls')
    print('<<MENU PILIHAN>>')
    print('1. Isi Data Buku')
    print('2. Tampil Data Buku')
    print('3. Urut Data Buku')
    print('0. Keluar')
    Menu = int(input('Pilihan Anda? '))
    return Menu

#subrutin menu pengurutan
def MenuUrut(Menu2):
    os.system('cls')
    print('<<MENU PENGURUTAN>>')
    print('1. Kode Buku')
    print('2. Nama Buku')
    print('3. Jenis Buku')
    print('4. Stok Buku')
    print('0. Kembali Ke Menu Pilihan')
    Menu2 = int(input('Pilihan Anda? '))
    return Menu2

#subrutin menentukan jenis buku 
def JenisBuku(Kode):
    if (Kode[0:3] == '000'):
        return 'Karya Umum'
    elif(Kode[0:3] == '100'):
        return 'Filsafat & Psikologi'
    elif(Kode[0:3] == '200'):
        return 'Agama'
    elif(Kode[0:3] == '300'):
        return 'Ilmu Politik & Ekonomi'
    elif(Kode[0:3] == '400'):
        return 'Bahasa'
    elif(Kode[0:3] == '500'):
        return 'Ilmu Pengetahuan Alam & Matematik'
    elif(Kode[0:3] == '600'):
        return 'Teknologi & Ilmu Terapan'
    elif(Kode[0:3] == '700'):
        return 'Seni Hiburan & Olahraga'
    elif(Kode[0:3] == '800'):
        return 'Kesustraan'
    else:
        return 'Sejarah & Geografi'

#subrutin memasukan larik buku
def IsiDataBuku(KB,NB,JB,SB,N):
    os.system('cls')
    print('PENGISIAN DATA BUKU')
    print('===================')
    i = 0
    print(f'<<DATA BUKU Ke-{i+1}')
    KB[i] = str(input('Kode Buku  :  ')).upper()
    while (KB[i] != 'STOP'):
        NB[i] = str(input('Nama Buku  :  ')).upper()
        JB[i] = JenisBuku(KB[i])
        print(f'Jenis Buku :  {JB[i]}')
        SB[i] = int(input('Stok Buku  :  '))

        #memasukan data buku selanjutnya
        print()
        i+=1
        print(f'<<DATA BUKU Ke-{i+1}')
        KB[i] = str(input('Kode Buku  :  ')).upper()

    N = i
    return N 

#subrutin mengurutkan kode buku secara asceding menggunakan Bubble Sort
def UrutKodeAsc(N,KB,NB,JB,SB):
    for i in range(N-1):
        for j in range(N,i,-1):
            if(KB[j] < KB[j-1]):
                #tukar kode buku
                temp = KB[j]
                KB[j] = KB[j-1]
                KB[j+1] = temp

                #tukar nama buku
                temp = NB[j]
                NB[j] = NB[j-1]
                NB[j+1] = temp

                #tukar jenis buku
                temp = JB[j]
                JB[j] = JB[j-1]
                JB[j+1] = temp

                #tukar stok buku
                temp = SB[j]
                SB[j] = SB[j-1]
                SB[j+1] = temp

#subrutin mengurutkan nama buku secara descending menggunaksn Bubble sort
def UrutNamaDsc(N,KB,NB,JB,SB):
    for i in range(N-1):
        for j in range(N-i):
            if(NB[j] < NB[j+1]):
                #tukar kode buku
                temp = KB[j]
                KB[j] = KB[j+1]
                KB[j-1] = temp

                #tukar nama buku11
                temp = NB[j]
                NB[j] = NB[j+1]
                NB[j-1] = temp

                #tukar jenis buku
                temp = JB[j]
                JB[j] = JB[j+1]
                JB[j-1] = temp

                #tukar stok buku
                temp = SB[j]
                SB[j] = SB[j+1]
                SB[j-1] = temp

#subrutin mengurutkan jenis buku secara asceding menggunakan Bubble Sort
def UrutJenisAsc(N,KB,NB,JB,SB):
    for i in range(1,N):
        max = 0
        for j in range(1,N+1,-i):
            if(JB[j] > JB[max]):
                max = j

            #tukar kode buku
            temp = KB[max]
            KB[max] = KB[j]
            KB[j] = temp

            #tukar nama buku
            temp = NB[max]
            NB[max] = NB[j]
            NB[j] = temp

            #tukar jenis buku
            temp = JB[max]
            JB[max] = JB[j]
            JB[j] = temp

            #tukar stok buku
            temp = SB[max]
            SB[max] = SB[j]
            SB[j] = temp

#subrutin menampilkan daftar buku dalam bentuk tabel
def TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N):
    os.system('cls')
    print('                                      Daftar Buku')
    print(f'Bulan : {Bulan}')
    print(f'Tahun : {Tahun}')
    print('-----------------------------------------------------------------------------------')
    print('| No | Kode Buku |      Nama Buku      |               Jenis               | Stok |')
    print('-----------------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>2} | {KB[i]:>9} | {NB[i]:>19} | {JB[i]:>33} | {SB[i]:4} |')
    print('-----------------------------------------------------------------------------------')


#badan program utama
os.system('cls')
#penciptaan larik kode buku(KB), nama buku (NB), jenis buku (JB), dtok buku(SB)
KB = ['/'] * MAKSBUKU
NB = ['/'] * MAKSBUKU
JB = ['/'] * MAKSBUKU
SB = [0] * MAKSBUKU
#memasukan bulan dan tahun
print('PENGISIAN DATA BUKU')
print('===================')
Bulan = str(input('Bulan : ')).upper()
Tahun = str(input('Tahun : '))
TampilBuku(Bulan,Tahun,KB,NB,JB,SB,MAKSBUKU)
print()
os.system('pause')

os.system('cls')
Menu = 0
Menu = MenuPilihan(Menu)
N = 0
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1:
            N = IsiDataBuku(KB,NB,JB,SB,N)
            TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
        case 2:
            if ( N > 0):      
                TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
            else:
                print('Isi Data Buku Terlebih Dahulu!')
                print()
                os.system('pause')
                N = IsiDataBuku(KB,NB,JB,SB,N)
        case 3:
            if ( N > 0):      
                Menu2 = 0
                Menu2 = MenuUrut(Menu2)
                while (Menu2 != 0):
                    os.system('cls')
                    match (Menu2):
                        case 1:
                            UrutKodeAsc(N,KB,NB,JB,SB)
                            TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
                        case 2:
                            UrutNamaDsc(N,KB,NB,JB,SB)
                            TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
                        case 3:
                            UrutJenisAsc(N,KB,NB,JB,SB)
                            TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
                        case 4:
                            #UrutStokDsc(N,KB,NB,JB,SB)
                            TampilBuku(Bulan,Tahun,KB,NB,JB,SB,N)
                        case _:
                            print('Nomor Menu Tidak Ada!')
                    os.system('pause')
                    os.system('cls')
                    Menu2 = MenuUrut(Menu2)
            else:
                print('Isi Data Buku Terlebih Dahulu!')
                print()
                os.system('pause')
                N = IsiDataBuku(KB,NB,JB,SB,N)
        case _: #validasi menu pilihan
            print('Nomor Menu Tidak Ada!')

    os.system('pause')
    os.system('cls')
    Menu = MenuPilihan(Menu)