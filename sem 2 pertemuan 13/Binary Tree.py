#program membuat biner tree
#I.S.:pengguna memasukan beberapa nama
#F.S.:menampilkan isi pohon biner
import os

#konstanta maksimal elemen nama
MAKSNAMA = 30

#pendefinisisan kelas
#1. kelas untuk node/simpul
class Node:
    #method inisialisasi 
    def __init__(self,Nama):
        self.Nama = Nama
        self.LS = None
        self.RS = None

#2. kelas untuk pohon biner
class BinaryTree:
    #method inisialisasi
    def __init__(self):
        self.Head = None
        self.Front = -1
        self.Rear = -1
        self.Queue = [' '] * MAKSNAMA
    #method membuat pohon biner
    def BuatPohonBiner(self,NamaBaru):
        if(self.Head is None):
            self.Head = Node(NamaBaru)
        else:
            self.BuatNodeBaru(NamaBaru,self.Head)
    
    #method membuat node baru pada pohon biner
    def BuatNodeBaru(self,NamaBaru,NodeParent):
        if (NamaBaru >= NodeParent.Nama):
            if (NodeParent.RS is None):
                NodeParent.RS = Node(NamaBaru)
            else:
                self.BuatNodeBaru(NamaBaru,NodeParent.RS)
        if (NamaBaru < NodeParent.Nama):
            if (NodeParent.LS is None):
                NodeParent.LS = Node(NamaBaru)
            else:
                self.BuatNodeBaru(NamaBaru,NodeParent.LS)
    
    #method cek queue kosong atau tidak 
    def Kosong(self): 
        return self.Rear == -1
    
    #method memasukan satu data di dalam queue (endqueue)
    def Enqueue(self,NamaBaru):     
        if(self.Kosong()):
            self.Front = 0
            self.Rear = 0
        else:
            self.Rear += 1
        self.Queue[self.Rear] = NamaBaru
        
    #method mengeluarkan satu data dari queue(Dequeue)
    def Dequeue(self):
        Item = self.Queue[self.Front]
        if (self.Rear == self.Front):
            self.Queue[self.Rear] = ' '
            self.Front = -1
            self.Rear = -1
        else:
            #lakukan pergeseran
            for i in range(self.Rear):
                self.Queue[i] = self.Queue[i+1]

            self.Queue[self.Rear] = ' '
            self.Rear -= 1
        return Item

    #menampilkan isi pohon biner
    def TampilPohonBiner(self,Root):
        if(self.Head is None):
            print('Pohon biner kosong')
        else:
            self.Enqueue(Root)
            print('| ',end='')
            while(not self.Kosong()):
                Simpul = self.Dequeue()
                print(Simpul.Nama,end=' | ')

                if (Simpul.LS):
                    self.Enqueue(Simpul.LS)
                if (Simpul.RS):
                    self.Enqueue(Simpul.RS)
            print()
    
    #menampilkan isi pohon biner per level
    def TampilPohonPerLevel(self,Root):
        if(self.Head is None):
            print('Pohon biner kosong')
        else:
            self.Enqueue(Root)
            Level = 1
            while(not self.Kosong()):
                BanyakElemen = self.Rear - self.Front+1
                print(f'level {Level} : ',end='')
                for i in range(BanyakElemen):
                    Simpul = self.Dequeue()
                    if( i> BanyakElemen-1):
                        print(', ',end='')
                    print(Simpul.Nama,end=' | ')

                    if (Simpul.LS):
                        self.Enqueue(Simpul.LS)
                    if (Simpul.RS):
                        self.Enqueue(Simpul.RS)
                Level += 1
                print()
            print()

#badan program utama
os.system('cls')
Pohon = BinaryTree()
Root = str(input('Masukan Nama Pertama (Root)   : ')).upper()
Pohon.BuatPohonBiner(Root)
NamaBaru = str(input('Masukan Nama Berikutnya (Root): ')).upper()
while(NamaBaru != 'STOP'):
    Pohon.BuatPohonBiner(NamaBaru)
    NamaBaru = str(input('Masukan Nama Berikutnya (Root): ')).upper()

print()
print('<<ISI POHON BINER>>')
Pohon.TampilPohonBiner(Pohon.Head)
print()
print('<<ISI POHON BINER PER LEVEL>>')
Pohon.TampilPohonPerLevel(Pohon.Head)