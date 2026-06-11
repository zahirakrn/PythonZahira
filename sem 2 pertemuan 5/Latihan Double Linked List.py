#nyoba doang eakkk
#Cibaduyut Banjir
#Kopo Tsunami
import os

# Class Node
class Node:
    def __init__(self, nim, nama, nilai):
        self.NIM = nim
        self.Nama = nama
        self.NA = nilai
        self.Next = None
        self.Prev = None


#  Class Node Double Linked List
class DoubleLinkedList:
    def __init__(self):
        self.Awal = None
        self.Akhir = None

    def Kosong(self):
        return self.Awal is None

# Tambah Data
    def TambahData(self, nim, nama, nilai):
        Baru = Node(nim, nama, nilai)

        if self.Kosong():
            self.Awal = Baru
            self.Akhir = Baru
        else:
            Baru.Prev = self.Akhir
            self.Akhir.Next = Baru
            self.Akhir = Baru

# Menampilkan dari belakang
    def TampilDariAkhir(self):
        if self.Kosong():
            print("List masih kosong!")
        else:
            Bantu = self.Akhir
            print("\n<< DATA DARI BELAKANG >>")
            while Bantu is not None:
                print(f"NIM   : {Bantu.NIM}")
                print(f"Nama  : {Bantu.Nama}")
                print(f"Nilai : {Bantu.NA}")
                print("----------------------")
                Bantu = Bantu.Prev

# Mencari nilai yang di atas rata-rata
    def CariDiAtasRata(self):
        if self.Kosong():
            print("List kosong!")
            return

        Bantu = self.Awal
        total = 0
        jumlah = 0

        while Bantu is not None:
            total += Bantu.NA
            jumlah += 1
            Bantu = Bantu.Next

        rata = total / jumlah
        print(f"\nRata-rata = {rata:.2f}")

        Bantu = self.Awal
        ketemu = False
        no = 0

        print("\n<< DI ATAS RATA-RATA >>")
        while Bantu is not None:
            if Bantu.NA > rata:
                ketemu = True
                no += 1
                print(f"\nData ke-{no}")
                print(f"NIM   : {Bantu.NIM}")
                print(f"Nama  : {Bantu.Nama}")
                print(f"Nilai : {Bantu.NA}")
            Bantu = Bantu.Next

        if not ketemu:
            print("Tidak ada yang di atas rata-rata")

# Subrutin Hapus Depan
    def HapusDepan(self):
        if self.Kosong():
            print("List kosong!")
        else:
            Phapus = self.Awal
            if self.Awal.Next is None:
                self.Awal = None
                self.Akhir = None
            else:
                self.Awal = self.Awal.Next
                self.Awal.Prev = None

            print(f"Data NIM {Phapus.NIM} dihapus")
            del Phapus

# Subrutin Hapus Belakang
    def HapusBelakang(self):
        if self.Kosong():
            print("List kosong!")
        else:
            Phapus = self.Akhir
            if self.Awal.Next is None:
                self.Awal = None
                self.Akhir = None
            else:
                self.Akhir = self.Akhir.Prev
                self.Akhir.Next = None

            print(f"Data NIM {Phapus.NIM} dihapus")
            del Phapus

# Subrutin Hapus Tengah
    def HapusTengah(self, nim):
        if self.Kosong():
            print("List kosong!")
            return

        Bantu = self.Awal
        Ketemu = False

        while (not Ketemu) and (Bantu is not None):
            if Bantu.NIM == nim:
                Ketemu = True
            else:
                Bantu = Bantu.Next

        if not Ketemu:
            print(f"NIM {nim} tidak ditemukan!")
        else:
            if Bantu is self.Awal:
                self.HapusDepan()
            elif Bantu is self.Akhir:
                self.HapusBelakang()
            else:
                Bantu.Prev.Next = Bantu.Next
                Bantu.Next.Prev = Bantu.Prev
                print(f"Data NIM {nim} dihapus")
                del Bantu

# Subrutin menu hapus
def MenuHapus():
    os.system('cls')
    print("<< MENU HAPUS >>")
    print("1. Hapus Depan")
    print("2. Hapus Belakang")
    print("3. Hapus Berdasarkan NIM")
    print("0. Kembali")
    return int(input("Pilih: "))

# Program Utama
List = DoubleLinkedList()

while True:
    os.system('cls')
    print("=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampil dari Belakang")
    print("3. Cari Nilai di Atas Rata-rata")
    print("4. Hapus Data")
    print("0. Keluar")

    pilih = int(input("Pilih: "))

    os.system('cls')
    match pilih:
        case 1:
            print("<< TAMBAH DATA >>")
            nim = input("NIM   : ")
            nama = input("Nama  : ")
            nilai = float(input("Nilai : "))
            List.TambahData(nim, nama, nilai)
            input("\nEnter...")

        case 2:
            List.TampilDariAkhir()
            input("\nEnter...")

        case 3:
            List.CariDiAtasRata()
            input("\nEnter...")

        case 4:
            menuHapus = -1
            while menuHapus != 0:
                menuHapus = MenuHapus()
                os.system('cls')

                match menuHapus:
                    case 1:
                        List.HapusDepan()
                        input("\nEnter...")

                    case 2:
                        List.HapusBelakang()
                        input("\nEnter...")

                    case 3:
                        nim = input("Masukkan NIM: ")
                        List.HapusTengah(nim)
                        input("\nEnter...")

                    case 0:
                        break

                    case _:
                        print("Menu tidak ada!")
                        input("\nEnter...")

        case 0:
            print("Keluar program...")
            break

        case _:
            print("Menu tidak ada!")
            input("\nEnter...")