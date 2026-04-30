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

    #method menambah saru data dibelakang
    def TambahDataMhs(self,MhsBaru):
        Baru = SimpulMhs(MhsBaru.NIM,MhsBaru.Nama,MhsBaru.NA,MhsBaru.Indeks)
        Baru.next = None
        if (self.Awal is None):
            Baru.Prev = None
            self.Awal = Baru
        else:
            Baru.Prev = self.Akhir
            self.Akhir.Next = Baru
        
        self.Akhir= Baru
    
    #method manampilkan data dari belakang
    def TampilDataMhs(self):
        print('--isi list mahasiswa--')
        if(self.Akhir is None):
            print('list mahasiswa masih kosong')
        else:
            Bantu = self.Akhir
            while(Bantu is not None):
                print(f'[{Bantu.Info.NIM}|{Bantu.Info.Nama}|{Bantu.Info.NA}|{Bantu.Info.Indeks}]',end='')
                if(Bantu is not self.Awal):
                    print('---> ', end= '')
                
                Bantu = Bantu.Prev

                print()

    #method Mencari Mahasiswa yang Nilai Akhirnya di atas rata rata
    def CariNA(self):
    #Mencari Rata-rata nilai
        Bantu = self.Awal
        TotalNilai = 0
        BanyakMhs = 0
        while (Bantu is not None):
            TotalNilai += Bantu.Info.NA
            BanyakMhs += 1
            Bantu = Bantu.Next
        
        Rerata = TotalNilai/BanyakMhs
        #Menampilkan Mahasiswa diatas rerata
        print(f'>> DAFTAR LIST MAHASISWA DIATAS RATA RATA {Rerata:.1f} <<')
        print('----------------------------------------------------------------------------')
        print('|NO|   NIM      |         NAMA                   | NILAI AKHIR    | INDEKS |')
        print('----------------------------------------------------------------------------')
        Bantu = self.Awal
        No= 0
        while (Bantu is not None):
            if(Bantu.Info.NA > Rerata):
                No +=1
                print (f'|{No:>2} |{Bantu.Info.NIM:>9} | {Bantu.Info.Nama:24}        | {Bantu.Info.NA:>15} | {Bantu.Info.Indeks:>1}|')

            Bantu = Bantu.Next
        print('----------------------------------------------------------------------------')

    #menghapus data mahasiswa tertentu
    def HapusDataMhs(self):
        NIMhapus = str(input('NIM YANG AKAN DIHAPUS : '))
        #mencari nim yang akan di hapus
        Phapus = self.Awal
        Ketemu = False
        while (not Ketemu) and (Phapus is not None):
            if (Phapus.Info.NIM == NIMhapus):
                Ketemu = True
            else:
                Phapus = Phapus.Next
        
        if(Ketemu):
            if(Phapus is self.Awal) and (Phapus is self.Akhir):
                self.Awal = None
                self.Akhir = None
            elif(Phapus is self.Awal): #ketemu di awal
                self.Awal = self.Awal.Next
                self.Awal.Prev = None
            elif (Phapus is self.Akhir):  # ketemu di akhir
                self.Akhir = self.Akhir.Prev
                self.Akhir.Next = None
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
    
    def UbahDataMhs(self):
        if self.Awal is None:
            print("List masih kosong!")
            
            return

        print("Cari berdasarkan:")
        print("1. Nama")
        print("2. Nilai Akhir")
        pilih = input("Pilihan: ")

        ketemu = False
        Bantu = self.Awal

        if pilih == '1':
            nama_cari = input("Masukkan nama yang dicari: ")

            while Bantu is not None:
                if Bantu.Info.Nama.lower() == nama_cari.lower():
                    ketemu = True
                    print("Data ditemukan:")
                    print(f"NIM  : {Bantu.Info.NIM}")
                    print(f"Nama : {Bantu.Info.Nama}")
                    print(f"NA   : {Bantu.Info.NA}")
                    print(f"Indeks : {Bantu.Info.Indeks}")

                    #ubah nama & nilai
                    Bantu.Info.Nama = input("Nama baru: ")
                    Bantu.Info.NA = int(input("Nilai Akhir baru: "))

                    #update indeks
                    Bantu.Info.Indeks = self.IndeksNilai(Bantu.Info.NA)

                    print("Data berhasil diupdate!\n")
                Bantu = Bantu.Next

        elif pilih == '2':
            nilai_cari = int(input("Masukkan nilai yang dicari: "))

            while Bantu is not None:
                if Bantu.Info.NA == nilai_cari:
                    ketemu = True
                    print("Data ditemukan:")
                    print(f"NIM  : {Bantu.Info.NIM}")
                    print(f"Nama : {Bantu.Info.Nama}")
                    print(f"NA   : {Bantu.Info.NA}")
                    print(f"Indeks : {Bantu.Info.Indeks}")

                    #ubah nama & nilai Akhir
                    Bantu.Info.Nama = input("Nama baru: ")
                    Bantu.Info.NA = int(input("Nilai Akhir baru: "))

                    #update indeks
                    Bantu.Info.Indeks = self.IndeksNilai(Bantu.Info.NA)

                    print("Data berhasil diupdate!\n")
                Bantu = Bantu.Next

        else:
            print("Pilihan tidak valid!")

        if not ketemu:
            print("Data tidak ditemukan!")

    #method menghancurkan seluruh simpul
    def Penghancuran(self):
        Phapus = self.Awal
        while (Phapus is not None):
            self.Awal = self.Awal.Next
            if (self.Awal is not None):
                self.Awal = None
            else:
                self.Akhir.Prev = None
                
            del(Phapus)
            Phapus = self.Awal

#subrutin menu pilihan
def MenuPilihan(Pilih):
    os.system('cls')
    print('==Menu Pilihan==')
    print('1. Tambah data')
    print('2. Tampil data')
    print('3. Cari data diatas rata-rata')
    print('4. Hapus data')
    print('5. Ubah data')
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
                ListMhs.UbahDataMhs()
                print()
                ListMhs.TampilDataMhs()
            else:
                print("Pilih Tambah data terlebih dahulu")

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
    print('list mahasiswa ')