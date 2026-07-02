#Program Antrian (Queue)
#I.S.: diberikan harga awal terhadap Front, Rear dan elemen Queue
#F.S.: menampilkan isi Queue Linear dan isi Queue Circular
import os

#konstanta maksimal nama kota
MAKSKOTA = 6

#pendefinisi kelas
#1. kelas queue linear
class QueueLinear:
    #method inisialisasi
    def __init__(self):
        self.Front = -1
        self.Rear = -1
        self.QueueKota = ['_'] * MAKSKOTA

    #method mengecek queue dalam keadaan kosong atau tidak
    def Kosong(self):
        return self.Rear == -1
    
    #method mengecek queue dalam keadaan penuh atau belum
    def Penuh(self):
        return self.Rear == MAKSKOTA-1

    #method menambahkan satu data ke Queue (Enqueue)
    def Enqueue(self, KotaBaru):
        if(not self.Penuh()):
            if(self.Kosong()):
                self.Front = 0
                self.Rear = 0
            else:
                self.Rear += 1
            
            self.QueueKota[self.Rear] = KotaBaru
        else:
            print("Queue Kota Penuh")

    #method menghapus satu data dari Queue (Dequeue)
    def Dequeue(self):
        if(not self.Kosong()):
            Item = self.QueueKota[self.Front]
            print(f'Kota yang keluar dari Queue: {Item}')
            if(self.Rear == self.Front):
                self.QueueKota[self.Rear] = '_'
                self.Front = -1
                self.Rear = -1
            else:
                #lakukan pergeseran data
                for i in range(self.Rear):
                    self.QueueKota[i] = self.QueueKota[i+1]

                self.QueueKota[self.Rear] = '_'
                self.Rear -= 1
        else:
            print("Queue Kota Kosong!")

    #method menampilkan isi Queue Linear
    def TampilQueue(self):
        print("<< ISI QUEUE LINEAR >>")
        print(f'Front = {self.Front+1}, Rear = {self.Rear+1}')
        print("Queue: ", end='')
        for i in range(MAKSKOTA):
            print(self.QueueKota[i], end='')
            if(i < MAKSKOTA - 1):
                print(',', end='')

        print()

#2. kelas queue circular
class QueueCircular:
    #method inisialisasi
    def __init__(self):
        self.Front2 = -1
        self.Rear2 = -1
        self.QueueKota2 = ['_'] * MAKSKOTA

    #method mengecek queue dalam keadaan kosong atau tidak
    def Kosong(self):
        return self.Rear2 == -1
    
    #method mengecek queue dalam keadaan penuh atau belum
    def Penuh(self):
        return (self.Front2 == 0 and self.Rear2 == MAKSKOTA-1) or (self.Front2 == self.Rear2 + 1)
    
    #method menambah saatu data ke dalam Queue (Enqueue)
    def Enqueue2(self, KotaBaru):
        if(not self.Penuh()):
            if(self.Kosong()):
                self.Front2 = 0
                self.Rear2 = 0
            else:
                if(self.Rear2 == MAKSKOTA-1):
                    self.Rear2 = 0
                else:
                    self.Rear2 += 1
            self.QueueKota2[self.Rear2] = KotaBaru
        else:
            print('Queue Kota Penuh!')

    def Dequeue2(self):
        if(not self.Kosong()):
            Item = self.QueueKota2[self.Front2]
            print(f'Kota yang keluar dari Queue: {Item}')
            self.QueueKota2[self.Front2] = '_'
            if(self.Rear2 == self.Front2):
                self.Front2 = -1
                self.Rear2 = -1
            else:
                if(self.Front2 == MAKSKOTA-1):
                    self.Front2 = 0
                else:
                    self.Front2 += 1
        else:
            print("Queue Kota Kosong!")

    def BanyakElemen2(self):
        if(self.Front2 <= self.Rear2):
            return (self.Rear2 - self.Front2 + 1)
        else:
            return (MAKSKOTA + self.Rear2 - self.Front2 + 1)

    #method menampilkan isi Queue CIRCULAR
    def TampilQueue2(self):
        print("<< ISI QUEUE CIRCULAR >>")
        print(f'Front = {self.Front2+1}, Rear = {self.Rear2+1}')
        print(f'Banyaknya Elemen di Queue = {self.BanyakElemen2()}')
        print("Queue: ", end='')
        for i in range(MAKSKOTA):
            print(self.QueueKota2[i], end='')
            if(i < MAKSKOTA - 1):
                print(',', end='')

        print()

#subrutin menu utama
def MENUUTAMA(Pilih):
    print('<-- MENU UTAMA -->')
    print('1. Tambah data ke Queue (Enqueue)')
    print('2. Hapus data dari Queue (Dequeue)')
    print('0. Keluar Program')
    Pilih = int(input('Pilihan Anda? '))
    return Pilih

#badan program utama
os.system('cls')
Queue = QueueLinear()
Queue2 = QueueCircular()

Pilih = 0
Pilih = MENUUTAMA(Pilih)
while Pilih != 0:
    os.system('cls')
    match(Pilih):
        case 1:
            print("<<PENAMBAHAN DATA KOTA INDONESIA KE QUEUE>>")
            KotaBaru = str(input('Nama Kota : ')).upper()
            os.system('cls')
            Queue.Enqueue(KotaBaru)
            Queue.TampilQueue()
            print()
            Queue2.Enqueue2(KotaBaru)
            Queue2.TampilQueue2()
            print()
            os.system('pause')
        case 2:
            print("<<PENGHAPUSAN DATA KOTA INDONESIA DARI QUEUE>>")
            os.system('cls')
            Queue.Dequeue()
            Queue.TampilQueue()
            print()
            Queue2.Dequeue2()
            Queue2.TampilQueue2()
            print()
            os.system('pause')
        case _:
            print('Nomor Menu Tidak Ada!')
            print()
            os.system('pause')
    os.system('cls')
    Pilih = MENUUTAMA(Pilih)
