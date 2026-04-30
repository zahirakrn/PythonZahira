#Program double Linked List Mahasiswa
#I.S.: pengguna memilih salah satu nomor menu
#F.S.:menampilkan hasil sesuai menu yang dipilih
import os

#pendefinisisan kelas untuk linkedlist
#1.memnuat kelas untuk record mahasiswa
class Mhs:
    def __init__(self,NIM,Nama,NA,Indeks):
        self.NIM = NIM
        self.Nama = Nama
        self.NA = NA
        self.Indeks = Indeks
#2.membuat kelas untuk simpul mahasiswa
class SimpulMhs:
    def __init__(self,NIM,Nama,NA,Indeks):
        self.Info = Mhs(NIM,Nama,NA,Indeks)
        self.Next = None
        self.Prev = None
#membuat kelas untuk double linked list
class DoubleLinkedList:
    def __init__(self):
        self.Awal = None
        self.Akhir = None


    #method Menemtukan Indeks Nilai
    def IndeksNilai (self,Nilai):
        if (78 <=Nilai<=100):
            return 'A'
        if (68 <=Nilai<=77):
            return 'B'
        if (56 <=Nilai<=67):
            return 'C'
        if (45<=Nilai<=55):
            return 'D'
        else:
            return 'E'

    #method menambah satu data dibelakang
    def TambahDataMhs(self,MhsBaru):
        Baru = SimpulMhs(MhsBaru.NIM,MhsBaru.Nama,MhsBaru.NA,MhsBaru.Indeks)
        if (self.Awal is None):
            self.Awal = Baru
        else:
            Baru.Prev = self.Akhir
            self.Akhir.Next = Baru
        
        self.Akhir= Baru
        #membuat circular 
        self.Awal.Prev = self.Akhir
        self.Akhir.Next = Baru
    
    #method manampilkan data dari depan
    def TampilDataMhs(self):
        print('--isi list mahasiswa--')
        if(self.Awal is None):
            print('list mahasiswa masih kosong')
        else:
            Bantu = self.Awal
            while(Bantu is not self.Akhir):
                print(f'[{Bantu.Info.NIM}|{Bantu.Info.Nama}|{Bantu.Info.NA}|{Bantu.Info.Indeks}]',end='')
                print('---> ', end= '')
                
                Bantu = Bantu.Next

            #menampilkan isi list di simpul terakhir 
            print(f'[{Bantu.Info.NIM}|{Bantu.Info.Nama}|{Bantu.Info.NA}|{Bantu.Info.Indeks}]')
                
           

    #method Mencari Mahasiswa yang Nilai Akhirnya di atas rata rata
    def CariNA(self):
    #Mencari Rata-rata nilai
        Bantu = self.Awal
        TotalNilai = 0
        BanyakMhs = 0
        while (Bantu is not self.Akhir):
            TotalNilai += Bantu.Info.NA
            BanyakMhs += 1
            Bantu = Bantu.Next
        #membuat circular
        TotalNilai += Bantu.Info.NA
        BanyakMhs += 1

        Rerata = TotalNilai/BanyakMhs
        #Menampilkan Mahasiswa diatas rerata
        print(f'>> DAFTAR LIST MAHASISWA DIATAS RATA RATA {Rerata:.1f} <<')
        print('----------------------------------------------------------------------------')
        print('| NO |   NIM     |         NAMA                    | NILAI AKHIR     | INDEKS |')
        print('----------------------------------------------------------------------------')
        Bantu = self.Awal
        No= 0
        while (Bantu is not self.Akhir):
            if(Bantu.Info.NA > Rerata):
                No +=1
                print (f'|{No:>2} |{Bantu.Info.NIM:>9} | {Bantu.Info.Nama:24}        | {Bantu.Info.NA:>15} | {Bantu.Info.Indeks:>5}|')

            Bantu = Bantu.Next
        
        #menampilkan isi list mahasiswa simpul terakhir
        if(Bantu.Info.NA > Rerata):
                No +=1
                print (f'|{No:>2} |{Bantu.Info.NIM:>9} | {Bantu.Info.Nama:24}        | {Bantu.Info.NA:>15} | {Bantu.Info.Indeks:>5}|')


        print('----------------------------------------------------------------------------')

    #Mencari Nilai Tertinggi dan Terendah
    def TinggiRendah(self):
        Bantu = self.Awal
        Tinggi = Bantu.Info.NA
        Rendah = Bantu.Info.NA
        while (Bantu is not self.Akhir):
            #menentukan Nilai Tertinggi
            if (Bantu.Info.NA >= Tinggi):
                Tinggi = Bantu.Info.NA

            #menentukan nilai Terendah
            if(Bantu.Info.NA < Rendah):
                Rendah = Bantu.Info.NA
            
            Bantu = Bantu.Next

        #Mengecek isi di simpul terakhir
        if (Bantu.Info.NA > Tinggi):
            Tinggi = Bantu.Info.NA

        if(Bantu.Info.NA < Rendah):
            Rendah = Bantu.Info.NA

        print(f'Nilai Tertinggi = {Tinggi}' )
        print(f'Nilai Terendah  = {Rendah}' )

    #menghapus data mahasiswa tertentu
    def HapusDataMhs(self):
        NIMhapus = str(input('NIM YANG AKAN DIHAPUS : '))
        #mencari nim yang akan di hapus
        Phapus = self.Awal
        Ketemu = False
        while (not Ketemu) and (Phapus is not self.Akhir):
            if (Phapus.Info.NIM == NIMhapus):
                Ketemu = True
            else:
                Phapus = Phapus.Next

        #mengecek isi simpul terakhir
        if (Phapus is self.Akhir)and (Phapus.Info.NIM == NIMhapus):
                Ketemu = True

        if(Ketemu):
            if(Phapus is self.Awal) and (Phapus is self.Akhir):
                self.Awal = None
                self.Akhir = None
            elif(Phapus is self.Awal): #ketemu di awal
                self.Awal = self.Awal.Next
                #membuat circular baru
                self.Awal.Prev = self.Akhir
                self.Akhir.Next = self.Awal
            elif (Phapus is self.Akhir):  # ketemu di akhir
                self.Akhir = self.Akhir.Prev
                #membuat circular baru
                self.Awal.Prev = self.Akhir
                self.Akhir.Next = self.Awal
            else:
                Phapus.Next.Prev = Phapus.Prev
                Phapus.Prev.Next = Phapus.Next

            os.system('cls')
            print('<<Data Mahasiswa yang di hapus >>')
            print(f' NIM                     : {NIMhapus}')
            print(f' Nama Mahasiswa          : {Phapus.Info.Nama}')
            print(f' Nilai Akhir             : {Phapus.Info.NA}')
            print(f' Indeks Nilai            : {Phapus.Info.Indeks}')
            del(Phapus)
        else:
            print(f'>> NIM {NIMhapus} TIDAK DI TEMUKAN << ' )
    
    #Method mengubah nama
    def UbahNama(self,Nimcari):
        Bantu = self.Awal
        Ketemu = False
        while(not Ketemu) and (Bantu is not self.Akhir):
            if(Bantu.Info.NIM == Nimcari):
                Ketemu = True
            else:
                Bantu = Bantu.Next

        #mengecek isi simpul terakhir
        if(Bantu is self.Akhir) and (Bantu.Info.NIM == Nimcari) :
            ketemu = True
        
        if(Ketemu):
            NamaUbah= str(input('nama {} diubah menjadi nama : '.format(Bantu.Info.Nama)))
            Bantu.Info.Nama= NamaUbah
        else:
            print(f'NIM {Nimcari} Tidak Ditemukan')
    
    #Method mengubah NILAI AKHIR
    def UbahNA(self,Nimcari):
        Bantu = self.Awal
        Ketemu = False
        while(not Ketemu) and (Bantu is not self.Akhir):
            if(Bantu.Info.NIM == Nimcari):
                Ketemu = True
            else:
                Bantu = Bantu.Next

        #mengecek isi simpul terakhir
        if(Bantu is self.Akhir) and (Bantu.Info.NIM == Nimcari) :
            ketemu = True
        
        if(Ketemu):
            NAUbah= int(input('Nilai Akhir {} diubah menjadi : '.format(Bantu.Info.NA)))
            Bantu.Info.NA= NAUbah
            Bantu.Info.Indeks = self.IndeksNilai(NAUbah)
        else:
            print(f'NIM {Nimcari} Tidak Ditemukan')

    #method menghancurkan seluruh simpul
    def Penghancuran(self):
        Phapus = self.Awal
        while (Phapus is not self.Akhir):
            self.Awal = self.Awal.Next
            #membuat circular baru
            self.Awal.Prev = self.Akhir
            self.Akhir.Next = self.Awal
            
            del(Phapus)
            Phapus = self.Awal
        
        del(Phapus)
        self.Awal = None
        self.Akhir = None

#subrutin menu pilihan
def MenuPilihan(Pilih):
    os.system('cls')
    print('==Menu Pilihan==')
    print('1. Tambah data')
    print('2. Tampil data')
    print('3. Cari data diatas rata-rata')
    print('4. Hapus data')
    print('5. Ubah data')
    print('6. Nilai Terendah Dan Terkecil')
    print('0. Keluar')
    Pilih = int(input('Pilihan anda? '))
    return Pilih

#badan program utama
ListMhs = DoubleLinkedList()
NIM = '/'
Nama='/'
NA = 0
Indeks = '/'
MhsBaru = Mhs(NIM,Nama,NA,Indeks)
Pilih = 0
Pilih = MenuPilihan(Pilih)
while (Pilih != 0):
    os.system('cls')
    match (Pilih):
        case 1 : #penambahan data dibelakang
            Lagi = 'Y'
            while (Lagi == 'Y'):
                os.system('cls')
                print('penambahan data mahasiswa dibelakang')
                MhsBaru.NIM     = str(input('NIM            : '))
                MhsBaru.Nama    = str(input('Nama Mahasiswa : '))
                MhsBaru.NA      = int(input('Nilai Akhir    : '))
                #Validasi Nilai akhir


                #memanggil fungsi indeks nilai
                MhsBaru.Indeks = ListMhs.IndeksNilai(MhsBaru.NA)
                ListMhs.TambahDataMhs(MhsBaru)
                print()
                ListMhs.TampilDataMhs()
                print()
                Lagi = str(input('tambah data lagi [Y/T]')).upper()
        case 2:
            ListMhs.TampilDataMhs()
            print()
            os.system('pause')
        case 3:
            if(ListMhs.Awal is not None):
                ListMhs.CariNA()
            else:
                print('Pilih Tambah data Terlebih Dahulu')  

            print()
            os.system('pause')
        case 4:#Menghapus data mahasiswa tertentu
            if(ListMhs.Awal is not None):
                ListMhs.HapusDataMhs()
            else:
                print('Pilih Tambah data Terlebih Dahulu')  

            print()
            os.system('pause')
        case 5:
            if(ListMhs.Awal is not None):
                print("PENGUBAHAN DATA MAHASISWA ")
                NIMcari = str(input(" Msukkan Nim Anda :"))
                print("1. Ubah Nama")
                print("2. Ubah Nilai")
                PilihUbah = int(input(" Pilihan Anda :"))
                match(PilihUbah):
                    case 1:
                        ListMhs.UbahNama(NIMcari)

                    case 2:
                        ListMhs.UbahNA(NIMcari)

                ListMhs.TampilDataMhs()
            else:
                print("Pilih Tambah data terlebih dahulu")

            print()
            os.system('pause')
        case 6:#Menampilkan nilai Tertinggi dan terendah
            if(ListMhs.Awal is not None):
                ListMhs.TampilDataMhs()
                print()
                ListMhs.TinggiRendah()
            else:
                print('Pilih Tambah data Terlebih Dahulu')  

            print()
            os.system('pause')
        case _:
            print('NOMOR MENU TIDAK ADA ')
            print()
            os.system('pause')

    os.system('cls')
    Pilih = MenuPilihan(Pilih)

ListMhs.Penghancuran()
if(ListMhs.Awal is None):
    print('list mahasiswa sudah Kosong ')