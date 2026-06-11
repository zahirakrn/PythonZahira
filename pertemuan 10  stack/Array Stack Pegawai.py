#Program Array Stack Pegawai
#I.S.: diberikan harga awal terhadap Top dan elemen array stack pegawai
#FF.S.: menampilkan isi stack pegawai
import os

#konstanta untuk maksimum elemen stack pegawai
MAKSPEGAWAI = 3

#pendefinisian stack pegawai
#1. membuat kelas untuk record pegawai
class DataPegawai:
    def __init__(self, NIP, Nama, Gol, GaPok, Status):
        self.NIP = NIP
        self.Nama = Nama
        self.Gol = Gol
        self.GaPok = GaPok
        self.Status = Status

#2. membuuat kelas untuk stack pegawai
class StackPegawai:
    #method inisialisasi
    def __init__(self):
        self.Top = -1
        self.Peg = [DataPegawai('/', '/', 0, 0, '/') for i in range(MAKSPEGAWAI)]

    #method menampilkan hasil inisialisasi
    def TampilInisialisasi(self):
        print('                 >> ISI STACK PEGAWAI (INISIALISASI) <<')
        print('+----------------------------------------------------------------------+')
        print('| No |    NIP    |    Nama Pegawai    | Gol. |   Gaji Pokok   | Status |')
        print('+----------------------------------------------------------------------+')
        for i in range(MAKSPEGAWAI -1, -1, -1):
            print(f'| {i+1:2} | {self.Peg[i].NIP:9} | {self.Peg[i].Nama:18} | {self.Peg[i].Gol:4} | Rp. {self.Peg[i].GaPok:10} |    {self.Peg[i].Status:1}   |')
        print('+----------------------------------------------------------------------+')

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top == -1

    #method mengecek stack penuh atau tidak
    def Penuh(self):
        return self.Top == MAKSPEGAWAI - 1
    
    #menentukan gaji pokok
    def GaPok(self,Gol):
        if Gol == 1:
            return 3500000
        elif Gol == 2:
            return 4500000
        elif Gol == 3:
            return 5500000
        else:
            return 0
        
    #method menambah 1 data ke dalam stack (push)
    def Push(self, PegMasuk : DataPegawai):
        if (not self.Penuh()):
            self.Top += 1
            PegBaru = DataPegawai(PegMasuk.NIP, PegMasuk.Nama, PegMasuk.Gol, PegMasuk.GaPok, PegMasuk.Status)
            self.Peg[self.Top] = PegBaru
        else:
            print('Stack Pegawai sudah penuh')

    #method mengeluarkan 1 data dari stack (pop)
    def Pop(self):
        if (not self.Kosong()):
            PegKeluar = self.Peg[self.Top]
            self.Peg[self.Top] = DataPegawai('/', '/', 0, 0, '/')
            self.Top -= 1
            print('-->DATA PEGAWAI KELUAR STACK<--')
            print(f'NIP          : {PegKeluar.NIP}')
            print(f'Nama Pegawai : {PegKeluar.Nama}')
            print(f'Golongan     : {PegKeluar.Gol}')
            print(f'Gaji Pokok   : Rp. {PegKeluar.GaPok}')
            print(f'Status       : {PegKeluar.Status}')
        else:
            print('Stack Pegawai kosong')
        
        os.system('pause')
                   
    #method menampilkan data pegawai 
    def TampilPegawai(self, N):
        os.system('cls')
        if(self.Kosong()):
            print('Stack Pegawai kosong')
        else:
            print('                        >> ISI STACK PEGAWAI <<')
            print(f'Posisi Top : {self.Top+1}')
            print('+----------------------------------------------------------------------+')
            print('| No |    NIP    |    Nama Pegawai    | Gol. |   Gaji Pokok   | Status |')
            print('+----------------------------------------------------------------------+')
            for i in range(N -1, -1, -1):
                print(f'| {i+1:2} | {self.Peg[i].NIP:9} | {self.Peg[i].Nama:18} | {self.Peg[i].Gol:4} | Rp. {self.Peg[i].GaPok:10} |    {self.Peg[i].Status:1}   |')
            print('+----------------------------------------------------------------------+')

#badan program utama
os.system('cls')
Stack = StackPegawai()
Stack.TampilInisialisasi()
os.system('pause')

#menambah daata pegawai ke dalam stack
Lagi = 'Y'
N = 0
while (Lagi == 'Y') and (not Stack.Penuh()):
    os.system('cls')
    print('                 >> PENAMBAHAN DATA PEGAWAI <<')
    N += 1
    print(f'PEGAWAI KE-{N}')
    print('------------------')
    NIP    = str(input('NIP                    : '))
    Nama   = str(input('Nama Pegawai           : ')).upper()
    Gol    = int(input('Golongan [1/2/3]       : '))
    Status = str(input('Status Pernikahan [M/B]: ')) .upper()
    GaPok  = Stack.GaPok(Gol)
    PegMasuk = DataPegawai(NIP, Nama, Gol, GaPok, Status)
    Stack.Push(PegMasuk)
    Stack.TampilPegawai(N)
    print()
    Lagi = str(input('Tambah data pegawai lagi? (Y/T): ')).upper()
    if (Stack.Top == MAKSPEGAWAI - 1) and (Lagi == 'Y'):
        print('Stack Pegawai sudah penuh')
        os.system('pause')

os.system('cls')
DataKeluar = str(input('Mau Mengeluarkan Data [Y/T]: ')).upper()
if (DataKeluar == 'Y'):
    Lagi = 'Y'
    while (Lagi == 'Y') and (not Stack.Kosong()):
        os.system('cls')
        Stack.Pop()
        N-= 1
        Stack.TampilPegawai(MAKSPEGAWAI)
        print()
        Lagi = str(input('Mengeluarkan Data Lagi? (Y/T): ')).upper()