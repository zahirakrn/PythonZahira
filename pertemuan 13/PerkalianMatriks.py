#program Perkalian 3 buah Matriks
#I.S.: pengguna memasukkan elemen 2 buah matriks (A dan B) borodo Baris x Kolom1
#F.S.: menampilkan matriks hasil penjumlhan (HasilJumlah) berordo Baris x Kolom1
import os

#konstanta
MAKSBARIS = 5
MAKSKOLOM1 = 10 
MAKSKOLOM2 = 5

def PenciptaanMatriks1(A, C):
    for j in range(MAKSBARIS):
        A[j] = [0] * MAKSKOLOM1

    for k in range(MAKSKOLOM1):
        C[k] = [0] * MAKSKOLOM2


def PenciptaanMatriks2(HasilKali):
    for k in range(MAKSBARIS):
        HasilKali[k] = [0] * MAKSKOLOM2


def TampilMatriks(Baris, Kolom1, Kolom2, A, C):
    os.system("cls")
    print(f"\033[34m<<ISI MATRIKS A BERORDO {Baris} x {Kolom1}>>\033[30m")
    for i in range(Baris):
        for j in range(Kolom1):
            print(f'{A[i][j]:>2} ',end='     ')
        print()

    print()
    print(f"\033[34m<<ISI MATRIKS C BERORDO {Kolom1} x {Kolom2}>>\033[30m")
    for j in range(Kolom1):
        for k in range(Kolom2):
            print(f'{C[j][k]} ',end='     ')
        print()

#subrutin mengisi elemen matriks A berordo Baris x Kolom1
def IsiMatriks2(Baris, Kolom1, Kolom2, A, C):
    print(f"\033[34m<<PENGISIAN MATRIKS A BERORDO {Baris} x {Kolom1}>>\033[30m")
    for i in range(Baris):
        for j in range(Kolom1):
            A[i][j] = int(input('A[{},{}] = '.format(i+1,j+1)))
        print()   

    print()
    print(f"\033[34m<<PENGISIAN MATRIKS C BERORDO {Kolom1} x {Kolom2}>>\033[30m")
    for j in range(Kolom1):
        for k in range(Kolom2):
            C[j][k] = int(input('C[{},{}] = '.format(j+1,k+1)))
        print()     

def Perkalian(Baris, Kolom1, Kolom2, A, C, HasilKali):
        for i in range(Baris):
            for j in range(Kolom2):
                HasilKali[i][j] = 0
                for k in range(Kolom1):
                    HasilKali[i][j] = HasilKali[i][j] + A[i][k] * C[k][j]

def TampilPerkalian(Baris, Kolom2, HasilKali):
    os.system("cls")
    print(f"\033[34m<<MATRIKS HASIL PERJUMLAHAN BERORDO {Kolom1} x {Kolom2}>>\033[30m")
    for i in range(Baris):
        for j in range(Kolom2):
            print(f'{HasilKali[i][j]:>2}', end='  ')
        print()

#badan program utama 
os.system("cls")
A = [0] * MAKSBARIS
C = [0] * MAKSKOLOM1
HasilKali = [0] * MAKSBARIS
PenciptaanMatriks1(A, C)
PenciptaanMatriks2(HasilKali)
TampilMatriks(MAKSBARIS, MAKSKOLOM1, MAKSKOLOM2, A, C)
print()
os.system("pause")

os.system("cls")
#memasukan banyaknya baris dan kolom 
Baris = int(input("Banyak Baris = "))
#validasi baris


Kolom1 = int(input("Banyak Kolom1 = "))
#validasi kolom

Kolom2 = int(input("Banyak Kolom2 = "))

os.system('cls')
IsiMatriks2(Baris, Kolom1, Kolom2, A, C)
TampilMatriks(Baris, Kolom1,Kolom2, A, C)
print()
os.system("pause")

os.system('cls')
Perkalian(Baris, Kolom1, Kolom2, A, C, HasilKali)
TampilPerkalian(Baris, Kolom2, HasilKali)
print()
os.system("pause")