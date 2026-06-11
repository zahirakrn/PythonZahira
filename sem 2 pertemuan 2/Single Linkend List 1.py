#Program Linked list 1 
#I.S. : diberikan harga awal terhadap pointer kepala (Awal)
#F.S.: menampilkan isi linked list
import os

#pendefinisian linked list
#1. membuat kelas untuk simpul
class Node:
    def __init__(self,Info):
        self.Info = Info 
        self.Next = None
    
#2.membuat kelas untuk single linked list
class SingleLinkedList:
    def __init__(self):
        self.Awal = None

    #method mengecek list kosong atau tidak
    def Kosong(self):
        kosong = False
        if (self.Awal is None):
            kosong = True

        return kosong
    
    #method menyisipkan satu simpuk di depan
    def SisipDepanSingle(self,AngkaBaru):
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
        if (self.Kosong()):
            self.Awal = Baru
        else:
            Bantu = self.Awal
            while (Bantu.Next is not None):
                Bantu = Bantu.Next
        Bantu.Next = Baru

    #method menyisipkan satu simpul setelah simpul tertentu
    def SisipTengahSingle(self,AngkaBaru):
        SisipSetelah = int(input('Angka {} disispkan setelah angka : '.format(AngkaBaru)))
        Bantu = self.Awal
        Ketemu = False
        while (not Ketemu) and (Bantu is not None):
            if (Bantu.Info == SisipSetelah):
                Ketemu = True
            else:
                Bantu = Bantu.Next

        if (Ketemu):
            Baru = Node(AngkaBaru)
            if (Bantu.Next is None):
                self.SisipBelakangSingle(AngkaBaru)
            else:
                Baru.Next = Bantu.Next
                Bantu.Next = Baru
        else:
            print(f'Angka {SisipSetelah} tidak di temukan')
            os.system('pause')
    
    #method menampilkan isi linked list
    def TampilData(self):
        print('<<ISI LINKED LIST>>')
        if (self.Kosong()):
            print('List Kosong. .')
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
        while (Phapus is None):
            self.Awal = self.Awal.Next
            del(Phapus)
            Phapus = self.Awal

#subrutin menu penyisipan
def MenuSisip(Menu):
    os.system('cls')
    print('<<MENU PENYISIPAN>>')
    print('1. Sisip Depan')
    print('2. Sisip Belakang')
    print('3. Sisip Tengah')
    print('0. Keluar')
    Menu = int(input('Pilihan Anda?'))
    return Menu

#badan program utama
#inisialisasi linked list
List = SingleLinkedList()

Menu = 0
Menu = MenuSisip(Menu)
while (Menu!= 0):
    os.system('cls')
    match (Menu):
        case 1:
            print('<<PENYISIPAN DI DEPAN>>')
            AngkaBaru = int(input('Masukan Sebuah Angka :'))
            List.SisipDepanSingle(AngkaBaru)
            #menampilkan isi linked list
            os.system('cls')
            List.TampilData()
            
            print()
            os.system('pause')
        case 2:
            print('<<PENYISIPAN DI BELAKANG>>')
            AngkaBaru = int(input('Masukan Sebuah Angka :'))
            List.SisipBelakangSingle(AngkaBaru)
            #menampilkan isi linked list
            os.system('cls')
            List.TampilData()
             
            print()
            os.system('pause')
        case 3:
            if(not List.Kosong()):
                print('<<PENYISIPAN DI TENGAH>>')
                AngkaBaru = int(input('Masukan Sebuah Angka :'))
                List.SisipTengahSingle(AngkaBaru)
                #menampilkan isi linked list
                os.system('cls')
                List.TampilData()
            else:
                print('Pilih Menu No.1 atau No.2 Terlebih Dahulu!')
        
            print()
            os.system('pause')
        case _:
            print('Nomor Menu Tidak Ada!')
            print()
            os.system('pause')

    os.system('cls')
    Menu = MenuSisip(Menu)

'''
#membuat dua buah simpul (Node1 dan Node2)
Node1 = Node(5) #Alloc(Node1) dan Node1^.Info <-- 5
Node2 = Node(15)

#menyambungkan simpul Node1 dengan simpul Node2
Node2.Next = None
Node1.Next = Node2

#menjadikan linked list 
List.Awal = Node1

#menampilkan isi linked list
os.system('cls')
List.TampilData()
print()
os.system('pause')

#menyisipkan satu simpul dibelakang (angka 3)
Node1 = Node(3)
Node1.Next = None
Node2.Next = Node1
#menampilkan isi linked list
print()
List.TampilData()
print()
os.system('pause')

#menyisipkan satu simpul di depan (angka 9)
Node2 = Node(9)
Node2.Next = List.Awal
List.Awal = Node2
#menampilkan isi linked list
print()
List.TampilData()
print()
os.system('pause')

#menyisipkan satu simpul dibelakang (angka 11)
Node2 = Node(11)
Node2.Next = None
Node1.Next = Node2
#menampilkan isi linked list
print()
List.TampilData()
print()
os.system('pause')
'''

#menghancurkan seluruh simpul
print()
List.Penghancuran()
if (List.Kosong()): 
    print('List Sudah Kosong. .')