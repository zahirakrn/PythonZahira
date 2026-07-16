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
        #inisialisasi pohon
        self.Head = None
        #inisialisasi queue linear
        self.Front = -1
        self.Rear = -1
        self.Queue = [' '] * MAKSNAMA
        #inisialisasi stack
        self.Top = -1
        self.Stack = [' '] * MAKSNAMA

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

    #method penelusuran preorder secara rekursif
    def Preorder(self,Simpul): #Node-Left-Right
        if (Simpul):
            print(Simpul.Nama,end='|')
            self.Preorder(Simpul.LS)
            self.Preorder(Simpul.RS)

    #method penelusuran preorder secara rekursif
    def Inorder(self,Simpul): #Left-Node-Right
        if (Simpul):
            self.Inorder(Simpul.LS)
            print(Simpul.Nama,end='|')
            self.Inorder(Simpul.RS)

     #method penelusuran preorder secara rekursif
    def Postorder(self,Simpul): #Left-Right-Node
        if (Simpul):
            self.Postorder(Simpul.LS)
            self.Postorder(Simpul.RS)
            print(Simpul.Nama,end='|')

    #method mengecek stack kosong atau tidak
    def StackKosong(self): 
        return self.Top == -1
    
    #method memasukan satu data ke dalam stack (push)
    def Push(self,Simpul):
        self.Top += 1
        self.Stack[self.Top] = Simpul

    #method mengeluarkan satu data dari stack (pop)
    def Pop(self):
        Item = self.Stack[self.Top]
        self.Stack[self.Top] = ' '
        self.Top -= 1
        return Item
    
    #method penelusuran preorder menggunakan stack
    def PreoerderStack(self,Simpul):
        while (not self.StackKosong()) or (Simpul is not None):
            print(Simpul.Nama,end='|')
            if (Simpul.LS is not None):
                if (Simpul.RS is not None):
                    self.Push(Simpul.RS)
                
                Simpul = Simpul.LS
            elif(Simpul.RS is not None):
                Simpul = Simpul.RS
            else: #jika tidak punya anak
                if (not self.StackKosong()):
                    Simpul = self.Pop()
                else:
                    Simpul = None

    #method penelusuran inorder menggunakan stack
    def InorderStack(self,Simpul): #Left-Node-Right
         while (not self.StackKosong()) or (Simpul is not None):
             if (Simpul is not None):
                self.Push(Simpul)
                Simpul = Simpul.LS
             else: #jika tidak punya anak
                Simpul = self.Pop()
                print(Simpul.Nama,end='|')
                Simpul = Simpul.RS
                  
    #method penelusuran postorder menggunakan stack
    #defPostorderStack(self,Simpul): #Left-Right-Node
        
   
    
    #method menghancurkan seluruh simpul di pohon biner
    def PenghancuranPohon(self,Simpul):
        if (Simpul is None):
            return
        
        self.PenghancuranPohon(Simpul.LS)
        self.PenghancuranPohon(Simpul.RS)
        if (Simpul == self.Head):
            self.Head = None
        Simpul.LS = None
        Simpul.RS = None
        del Simpul

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
print()

print('<< PENELUSURAN POHON BINER >>')
print('Preorder (Rekursif)   : ' ,end='')
Pohon.Preorder(Pohon.Head)
print()
print('Preorder (Stack)      : ' ,end='')
Pohon.PreoerderStack(Pohon.Head)
print()
print()
print('Inorder (Rekursif)    : ' ,end='')
Pohon.Inorder(Pohon.Head)  
print() 
print('Inorder (Stack)       : ' ,end='')
Pohon.InorderStack(Pohon.Head)  
print()
print()
print('Postorder (Rekursif)   : ' ,end='')
Pohon.Postorder(Pohon.Head)  
print()
os.system('pause')
os.system('cls')
Pohon.PenghancuranPohon(Pohon.Head)
Pohon.TampilPohonBiner(Pohon.Head)