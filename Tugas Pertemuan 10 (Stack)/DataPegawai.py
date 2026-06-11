# Program Data Pegawai
# I.S. : Pengguna memilih operasi pada stack dan memasukkan data pegawai
#        berupa NIP, Nama, Golongan, dan Status.
# F.S. : Data pegawai diproses sesuai operasi stack yang dipilih dan
#        hasilnya ditampilkan ke layar.

#NIM: 10125140
#NAMA: ZAHIRA KURNIA ANANDITA

import os

# Class Data Pegawai
class DataPegawai:
    def __init__(self, NIP, Nama, Gol, Gapok, Status):
        self.NIP = NIP
        self.Nama = Nama
        self.Gol = Gol
        self.Gapok = Gapok
        self.Status = Status


# Class Node
class NodePegawai:
    def __init__(self, data):
        self.Peg = data
        self.Next = None


# Mengecek stack kosong
def Kosong(Top):
    return Top is None


# Mengecek satu simpul
def SatuSimpul(Top):
    if Kosong(Top):
        return False
    return Top.Next is None


# Menentukan gaji pokok
def GajiPokok(Gol):
    if Gol == 1:
        return 3500000
    elif Gol == 2:
        return 4500000
    elif Gol == 3:
        return 5500000
    else:
        return 0


# Menampilkan keterangan status
def KeteranganStatus(Status):
    if Status == "M":
        return "Menikah"
    elif Status == "B":
        return "Belum Menikah"
    else:
        return "Tidak Valid"


def Push(Top, PegMasuk):

    NodeBaru = NodePegawai(PegMasuk)

    if Kosong(Top):
        Top = NodeBaru
    else:
        NodeBaru.Next = Top
        Top = NodeBaru

    return Top

def Pop(Top):

    if Kosong(Top):
        print("Stack kosong! Tidak dapat melakukan Pop.")
        return Top, None

    PegKeluar = Top.Peg

    if SatuSimpul(Top):
        Top = None
    else:
        Top = Top.Next

    return Top, PegKeluar


#Menampilkan Data Stack
def TampilStack(Top):

    if Kosong(Top):
        print("Data Stack Kosong")
        return

    Bantu = Top
    No = 1

    print("===============================================================================")
    print("| No | NIP        | Nama Pegawai         | Gol | Gaji Pokok      | Status     |")
    print("===============================================================================")

    while Bantu is not None:

        Peg = Bantu.Peg

        print(f"| {No:<2} | {Peg.NIP:<10} | {Peg.Nama:<20} | {Peg.Gol:<3} | {Peg.Gapok:<15} | {KeteranganStatus(Peg.Status):<14} |")
        Bantu = Bantu.Next
        No += 1

    print("===============================================================================")


# Penghancuran Stack
def Penghancuran(Top):

    while not Kosong(Top):

        Hapus = Top
        Top = Top.Next
        del Hapus

    print("Seluruh data stack berhasil dihancurkan.")
    return Top


#program utama

Top = None

while True:

    os.system('cls')

    print("===== MENU STACK DATA PEGAWAI =====")
    print("1. Tambah (Push)")
    print("2. Hapus (Pop)")
    print("3. Tampil Stack")
    print("4. Cek Kosong")
    print("5. Penghancuran")
    print("0. Keluar")

    Pilihan = input("Pilih Menu : ")

    
    if Pilihan == "1":

        Lagi = "Y"

        while Lagi == "Y":

            os.system('cls')

            print("<<< MENU PUSH PEGAWAI >>>")

            NIP = input("NIP            : ")
            Nama = input("Nama Pegawai   : ")
            Gol = int(input("Golongan (1-3) : "))

            Gapok = GajiPokok(Gol)

            print("Gaji Pokok     :", Gapok)
            print("M = Menikah")
            print("B = Belum Menikah")

            Status = input("Status (M/B)   : ").upper()

            data = DataPegawai(NIP,Nama,Gol,Gapok,Status)

            Top = Push(Top, data)

            print("Data berhasil ditambahkan.")

            TampilStack(Top)

            Lagi = input("Apakah ingin Push Data Lagi [Y/T] : ").upper()


    elif Pilihan == "2":

        os.system('cls')

        Top, PegKeluar = Pop(Top)

        if PegKeluar is not None:

            print("DATA PEGAWAI YANG DIHAPUS")
            print("========================")
            print("NIP         :", PegKeluar.NIP)
            print("Nama        :", PegKeluar.Nama)
            print("Golongan    :", PegKeluar.Gol)
            print("Gaji Pokok  :", PegKeluar.Gapok)
            print("Status      :", KeteranganStatus(PegKeluar.Status))

        input("Tekan Enter untuk kembali...")

    elif Pilihan == "3":

        os.system('cls')

        TampilStack(Top)

        input("Tekan Enter untuk kembali...")

    
    elif Pilihan == "4":

        os.system('cls')

        if Kosong(Top):
            print("Stack Kosong")
        else:
            print("Stack Tidak Kosong")

        input("Tekan Enter untuk kembali...")

    
    elif Pilihan == "5":

        os.system('cls')

        Top = Penghancuran(Top)

        input("Tekan Enter untuk kembali...")

    
    elif Pilihan == "6":

        print("Program selesai.")

    else:

        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")