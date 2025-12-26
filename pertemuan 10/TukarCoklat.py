#Program Menukarkan Bungkus Coklat
#I.S.: pengguna memasukan banyaknya bungkus coklat yang akan di tukar
#F.S.: menampilkan jumlah coklat yang diterima
import os

#konstanta
USERNAME = 'Jira'

PASSWORD = '10125140'

#subrutin masukkan nama pengguna
def IsiPengguna(Pengguna):
    print('\033[34m--Halaman Masuk Pengguna--\033[30m')
    Pengguna = str(input('Nama Pengguna : '))
    return Pengguna
#subrutin masukkan kata sandi
def IsiKataSandi(KataSandi):
    KataSandi = str(input('Kata Sandi    : '))
    return KataSandi

#subrutin mengecek login yang dimasukan pengguna
def CekLogin(Pengguna,KataSandi):
    Salah = 0
    while ((Pengguna != USERNAME) or (KataSandi != PASSWORD) and (Salah <3)):
        Salah = Salah + 1
        if(Salah == 3):
            print('\033[31mMaaf, Anda Sudah 3x Gagal Masuk Program!\033[30m')
        else:
            print('\033[34mNama Pengguna atau Kata Sandi Salah!\033[30m')
            os.system('pause')
            os.system('cls')
            Pengguna = IsiPengguna(Pengguna)
            KataSandi = IsiKataSandi(KataSandi)
    return Salah    

#subrutin memasukkan banyaknya bungkus coklat yang akan di tukar
def IsiBanyakBungkus(BanyakBungkus):
    BanyakBungkus = int(input('Banyaknya Bungkus Coklat : '))
    while (BanyakBungkus < 3) or (BanyakBungkus > 100):
        print('\033[31mBungkus Coklat yang di tukar hanya 3 - 100 bungkus!\033[30m')
        os.system('pause')    
        os.system('cls')
        print('\033[34m<<PROGRAM MENUKARKAN BUNGKUS COKLAT>>\033[30m')
        BanyakBungkus = int(input('Banyaknya Bungkus Coklat : '))
    return BanyakBungkus 

#subrutin menghitung jumlah coklat yang diterima
def BanyakCoklat(BanyakBungkus):
    Coklat = 0
    while (BanyakBungkus > 3):
        Coklat = Coklat + BanyakBungkus // 3
        Sisa =  BanyakBungkus % 3
        BanyakBungkus = BanyakBungkus // 3 + Sisa

        return Coklat  

#subrutin menampilkan jumlah coklat yang diterima
def TampilCoklat(BanyakBungkus):
    print(f'Coklat yang diterima : \033[31m{BanyakCoklat(BanyakBungkus)}\033[30m pcs')


#badan program
os.system('cls')
Pengguna = ''
Pengguna = IsiPengguna(Pengguna)
KataSandi = ''
KataSandi = IsiKataSandi(KataSandi)


if(CekLogin(Pengguna,KataSandi) < 3):
    os.system('cls')
    print('\033[33m<<PROGRAM MENUKARKAN BUNGKUS COKLAT>>\033[30m')
    BanyakBungkus = 0
    BanyakBungkus = IsiBanyakBungkus(BanyakBungkus)
    TampilCoklat(BanyakBungkus)
    



