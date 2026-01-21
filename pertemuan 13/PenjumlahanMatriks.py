#Program Penjumlahan 2 buah Matriks
#I.S.: Pengguna memasukkan elemen 2 buah matriks (A dan B) berordo Baris x Kolom1
#F.S.: Menampilkan matriks hasil penjumlahan (HasilJumlah) berordo Baris x Kolom1
import os

#kontanta
MAKSBARIS = 10
MAKSKOLOM1 = 10

#subrutin penciptaan matriks
def PenciptaanMatriks1(A, B, HasilJumlah):
    for j in range (MAKSBARIS) :
        A[j] = [0] * MAKSKOLOM1
        B[j] = [0] * MAKSKOLOM1
        HasilJumlah[j] = [0] * MAKSKOLOM1

#subrutin menampilkan elemen matriks A dan matriks B
def TampilMatriks(Baris,Kolom1,A,B): 
    os.system('cls')
    print(f'\033[36m<<ISI MATRIKS A BERORDO {Baris} x {Kolom1}>>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            print(f'{A[i][j]:>2}', end='     ')
        print()

    print()
    print(f'\033[36m<<ISI MATRIKS B BERORDO {Baris} x {Kolom1}>>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            print(f'{B[i][j]:>2}', end='     ')
        print()

#subrutin Mengisi elemen matriks A dan matriks B berordo Baris x Kolom1
def IsiMatriks1(Baris,Kolom1,A,B): 
    print(f'\033[36m<<ISI MATRIKS A BERORDO {Baris} x {Kolom1}>>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            A[i][j] = int(input('A[{},{}] = '.format(i+1,j+1)))
        print()

    print()
    print(f'\033[36m<<ISI MATRIKS B BERORDO {Baris} x {Kolom1}>>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            B[i][j] = int(input('B[{},{}] = '.format(i+1,j+1)))
        print()

#subruitn menjumlahkan dua buah matriks (A dan B)
def Penjumlahan (Baris,Kolom1,A,B,HasilJumlah): 
    for i in range(Baris):
        for j in range(Kolom1):
            HasilJumlah[i][j] = A[i][j] + B[i][j]

#subrutin menampilkan hasil penjumlahan
def TampilJumlah(Baris, Kolom1, HasilJumlah):
    os.system('cls')
    print(f'\033[36m<<HASIL PENJUMLAHAN MATRIKS A DAN B BERORDO {Baris} x {Kolom1}>>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            print(f'{HasilJumlah[i][j]:>2}', end='     ')
        print()

#Badan Program Utama
os.system('cls')
A = [0] * MAKSBARIS
B = [0] * MAKSBARIS
HasilJumlah = [0] * MAKSBARIS
PenciptaanMatriks1(A,B,HasilJumlah)
TampilMatriks(MAKSBARIS,MAKSKOLOM1,A,B)
print()
os.system('pause')

os.system('cls')
#memasukkan banyaknya baris dan kolom
Baris = int(input('Banyak Baris = '))
#validasi baris

Kolom1 = int(input('Banyak Kolom = '))
#validasi kolom 

os.system('cls')
IsiMatriks1(Baris, Kolom1,A,B)
TampilMatriks(Baris,Kolom1,A,B)
print()
os.system('pause')

os.system('cls')
Penjumlahan(Baris, Kolom1,A,B,HasilJumlah)
TampilJumlah(Baris,Kolom1,HasilJumlah)
print()
os.system('pause')