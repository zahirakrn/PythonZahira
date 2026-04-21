#Program Single Linked List 2
#I.S.: Diberikan harga awal terhadap pointer kepala(Awal)
#F.S.: Menampilkan isi linked list
import os

#pendefinisian linked list 
#1. membuat kelas untuk simpulnya 
class Node:
    def __init__(self,Info):
        self.Info = Info
        self.Next = None

#2. Membuat kelas untuk single linked list
class SingleLinkedList:
    def __init__(self):
        self.Awal = None

    #method mengecheck list kosong atau tidak
    def Kosong(self):
        kosong = False
        if(self.Awal is None):
            kosong = True

        return kosong 
    
    #method menyisipkan satu simpul di depan
    def SisipDepanSingle (self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if (self.Kosong()):
            Baru.Next = None
        else:
            Baru.Next = self.Awal

        self.Awal = Baru

    #method menyisipkan satu simpul di belakang
    def SisipBelakangSingle(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        Baru.Next = None
        if(self.Kosong()):
            self.Awal = Baru
        else:
            Bantu = self.Awal
            while (Bantu.Next is not None):
                Bantu = Bantu.Next

            Bantu.Next = Baru

    #method menyisipkan satu simpul di tengah
    def SisipTengahSingle(self,AngkaBaru):
        SisipSetelah = int(input('Angka {} disisipkan setelah angka : '.format(AngkaBaru)))
        Bantu = self.Awal
        Ketemu = False
        while (not Ketemu) and (Bantu is not None):
            if (Bantu.Info == SisipSetelah):   
                Ketemu = True
            else:
                Bantu = Bantu.Next

        if(Ketemu):
            Baru = Node(AngkaBaru)
            if (Bantu.Next is None):
                self.SisipBelakangSingle(AngkaBaru)
            else:
                Baru.Next = Bantu.Next
                Bantu.Next = Baru
        else: #jika tidak ditemukan
            print(f'Angka {SisipSetelah} tidak ditemukan!')
            os.system('pause')   

    #method mengubah data
    def UbahData(self,AngkaBaru):
        AngkaUbah = int(input("Angka Yang Akan Diubah : "))
        Bantu = self.Awal
        Ketemu = False
        while (not Ketemu) and (Bantu is not None):
            if (Bantu.Info == AngkaUbah):
                Ketemu = True
            else:
                Bantu = Bantu.Next

        if (Ketemu):
            Bantu.Info = AngkaBaru
        else:
            print(f"Angka {AngkaUbah} Yang Akan Diubah Tidak Ada!")
            print()
            os.system('pause')

    #method hapus depan 
    def HapusDepanSingle(self):
        if(self.Kosong()):
            print("List Kosong!")
            os.system('pause')
        else:
            Phapus = self.Awal
            self.Awal = self.Awal.Next
            del(Phapus)

    #method hapus belakang 
    def HapusBelakangSingle(self):
        if(self.Kosong()):
            print("List Kosong!")
            os.system('pause')
        else:
            if(self.Awal.Next is None):
                del(self.Awal)
                self.Awal = None
            else:
                Bantu = self.Awal
                while(Bantu.Next.Next is not None):
                    Bantu = Bantu.Next

                Phapus = Bantu.Next
                Bantu.Next = None
                del(Phapus)

    #method menghapus satu simpul di tengah
    def HapusTengahSingle(self):
        if (self.Kosong()): 
            print('List Kosong!')
            print()
            os.system('pause')
        else:
            HapusAngka = int(input('Angka Yang Akan Dihapus : '))
            Phapus = self.Awal
            Ketemu = False
            while (not Ketemu) and (Phapus is not None):
                if (Phapus.Info == HapusAngka):
                    Ketemu = True
                else: 
                    Phapus = Phapus.Next

            if (Ketemu):
                AngkaHapus = Phapus.Info
                if (Phapus is self.Awal):
                    self.HapusDepanSingle()
                elif (Phapus.Next is None):
                    self.HapusBelakangSingle()
                else:
                    Bantu = self.Awal
                    while (Bantu.Next is not Phapus):
                        Bantu = Bantu.Next

                    Bantu.Next = Phapus.Next
                    del(Phapus)
                
                print(f'Data yang dihapus : {AngkaHapus}')
            else:
                print(f'Angka {HapusAngka} yang akan dihapus tidak ditemukan!')
                print()
                os.system('pause')

    #method pencarian data 
    def PencarianData(self):
        if(self.Kosong()):
            print("List Masih Kosong!")
            print()
            os.system('pause')
        else:
            CariAngka = int(input("Masukkan Angka Yang Dicari : "))
            Bantu = self.Awal
            Ketemu = False
            Posisi = 1

            while(Bantu is not None):
                if(Bantu.Info == CariAngka):
                    Ketemu = True
                    break
                else:
                    Bantu = Bantu.Next
                    Posisi += 1

            if(Ketemu):
                print(f"Angka {CariAngka} ditemukan pada posisi ke-{Posisi}")
            else:
                print(f"Angka {CariAngka} tidak ditemukan!")

            print()
            os.system('pause')
    
    #method pengurutan data secara ascending 
    def PengurutanData(self):
        if(self.Kosong()):
            print("List Masih Kosong!")
            print()
        else:
            i = self.Awal
            while(i is not None):
                j = i.Next
                while(j is not None):
                    if(i.Info > j.Info):
                        Temp = i.Info
                        i.Info = j.Info
                        j.Info = Temp
                    j = j.Next
                i = i.Next

            print("Data Berhasil Diurutkan (Ascending)!")

    #method pengurutan data secara descending 
    def PengurutanDataDec(self):
        if(self.Kosong()):
            print("List Masih Kosong!")
            print()
        else:
            i = self.Awal
            while(i is not None):
                j = i.Next
                while(j is not None):
                    if(i.Info < j.Info):   
                        Temp = i.Info
                        i.Info = j.Info
                        j.Info = Temp
                    j = j.Next
                i = i.Next

            print("Data Berhasil Diurutkan (Descending)!")

    
    #method menampilkan isi linked list
    def TampilData(self):
        print('<< ISI LINKED LIST >>')
        if (self.Kosong()):
            print('List Kosong')
        else:
            Bantu = self.Awal
            while (Bantu is not None):
                print(Bantu.Info,end='')
                if (Bantu.Next is not None):
                    print(' --> ', end='')

                Bantu = Bantu.Next


    #method menghancurkan seluruh simpul
    def Penghancuran(self):
        Phapus = self.Awal
        while (Phapus is not None):
            self.Awal = self.Awal.Next 
            del(Phapus)
            Phapus = self.Awal

#Subrutin menu penyisipan
def MenuSisip(Menu):
    os.system('cls')
    print('<<MENU PENYISIPAN>>')
    print('1. Sisip Depan')
    print('2. Sisip Belakang')
    print('3. Sisip Tengah')
    print('0. Keluar')
    Menu = int(input('Pilihan Anda? '))
    return Menu

#Subrutin menu penghapusan
def Menu_Hapus(MenuHapus):
    os.system('cls')
    print('<<MENU PENGHAPUSAN>>')
    print('1. Hapus Depan')
    print('2. Hapus Belakang')
    print('3. Hapus Tengah')
    print('0. Keluar')
    MenuHapus = int(input('Pilihan Anda? '))
    return MenuHapus

#Subrutin menu pengurutan
def Menu_Urut(MenuUrut):
    os.system('cls')
    print('<<MENU PENGURUTAN>>')
    print('1. Ascending')
    print('2. Descending')
    print('0. Keluar')
    MenuUrut = int(input('Pilihan Anda? '))
    return MenuUrut

#Subrutin menu utama
def Menu_Utama(MenuUtama):
    os.system('cls')
    print('<<MENU UTAMA>>')
    print('1. Penambahan/Penyisipan Data')
    print('2. Pengubahan Data')
    print('3. Penghapusan Data')
    print('4. Pencarian Data')
    print('5. Pengurutan Data')
    print('6. Penyajian Data')
    print('0. Keluar')
    MenuUtama = int(input('Pilihan Anda? '))
    return MenuUtama

#Badan Program Utama
#inisialisasi linked list
List = SingleLinkedList()

MenuUtama = 0
MenuUtama = Menu_Utama(MenuUtama)
while (MenuUtama != 0):
    os.system('cls')
    match(MenuUtama):
        case 1:
            #penambahan data
            Menu = 0
            Menu = MenuSisip(Menu)
            while (Menu != 0):
                os.system('cls')
                match (Menu):
                    case 1:
                        print('<<PENYISIPAN DI DEPAN>>')
                        AngkaBaru = int(input('Masukkan Sebuah Angka : '))
                        List.SisipDepanSingle(AngkaBaru)
                        
                        #Menampilkan isi linked list
                        os.system('cls')
                        List.TampilData()
                        
                        print()
                        os.system('pause')
                    case 2:
                        print('<<PENYISIPAN DI BELAKANG>>')
                        AngkaBaru = int(input('Masukkan Sebuah Angka : '))
                        List.SisipBelakangSingle(AngkaBaru)

                        #Menampilkan isi linked list
                        os.system('cls')
                        List.TampilData()
                        
                        print()
                        os.system('pause')
                    case 3:
                        if(not List.Kosong()):
                            print('<<PENYISIPAN DI TENGAH>>')
                            AngkaBaru = int(input('Masukkan Sebuah Angka : '))
                            List.SisipTengahSingle(AngkaBaru)
                        
                            #Menampilkan isi linked list
                            os.system('cls')
                            List.TampilData()
                        else:
                            print('Pilih Menu No.1 atau No.2 Terlebih Dahulu')
                        print()
                        os.system('pause')
                    case _:
                        print('Nomor Menu Tidak Ada!')
                        
                        print()
                        os.system('pause')

                os.system('cls')
                Menu = MenuSisip(Menu)
        case 2:
            #pengubahan data
            if (List.Kosong()):
                print("List Masih Kosong!")
            else:
                print('<<PENGUBAHAN DATA>>')
                AngkaBaru = int(input('Masukkan Sebuah Angka : '))
                List.UbahData(AngkaBaru)
                List.TampilData()
            
            print()
            os.system('pause')
        case 3:
            MenuHapus = 0
            MenuHapus = Menu_Hapus(MenuHapus)
            while(MenuHapus != 0):
                os.system('cls')
                match (MenuHapus):
                    case 1: #penghapusan di depan
                        print('<<PENGHAPUSAN DI DEPAN>>')
                        List.HapusDepanSingle()
                        List.TampilData()
                        print()
                        os.system('pause')
                    case 2: #penghapusan di belakang
                        print('<<PENGHAPUSAN DI BELAKANG>>')
                        List.HapusBelakangSingle()
                        List.TampilData()
                        print()
                        os.system('pause')
                    case 3: #penghapusan di Tengah
                        print('<<PENGHAPUSAN DI TENGAH>>')
                        List.HapusTengahSingle()
                        List.TampilData()
                        print()
                        os.system('pause')
                    case _: #validasi menu penghapusan
                        print('Nomor Menu Tidak Ada!')
                        print()
                        os.system('pause')

                os.system('cls')
                MenuHapus = Menu_Hapus(MenuHapus)

        case 4:
            #pencarian data
            os.system('cls')
            print('<<PENCARIAN DATA>>')
            List.PencarianData()

        case 5:
            #pengurutan data
            MenuUrut = 0
            MenuUrut = Menu_Urut(MenuUrut)

            while(MenuUrut != 0):
                os.system('cls')
                match(MenuUrut):
                    case 1:
                        print('<<PENGURUTAN ASCENDING>>')
                        List.PengurutanData()
                        List.TampilData()
                        print()
                        os.system('pause')

                    case 2:
                        print('<<PENGURUTAN DESCENDING>>')
                        List.PengurutanDataDec()
                        List.TampilData()
                        print()
                        os.system('pause')

                    case _:
                        print('Nomor Menu Tidak Ada!')
                        print()
                        os.system('pause')

                os.system('cls')
                MenuUrut = Menu_Urut(MenuUrut)

        case 6:
            #penyajian data
            os.system('cls')
            List.TampilData()

            print()
            os.system('pause')
        case _:
            #validasi menu utama
            print('Nomor Menu Tidak Ada!')
            print()
            os.system('pause')

    os.system('cls')
    MenuUtama = Menu_Utama(MenuUtama)


#menghancurkan seluruh simpul
print()
List.Penghancuran()
if (List.Kosong()):
    print('List Sudah Kosong')