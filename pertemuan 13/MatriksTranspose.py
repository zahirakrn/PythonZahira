#Program Matriks Transpose
#I.S.: pengguna memasukan elemen matriks A berordo Baris x Kolom
#F.S.: menampilkan matriks transpose A berordo Kolom1 x Baris
import os 

#konstantan
MAKSBARIS = 10
MAKSKOLOM1 = 10

#subrutin penciptaan matriks
def PenciptaanMatriks1(A,ATranspose):
    for j in range(MAKSBARIS):
        A[j] = [0] * MAKSKOLOM1   

    for i in range(MAKSKOLOM1):
        ATranspose[i] = [0] * MAKSBARIS

#subrutin menampilkan elemen matriks A
def TampilMatriks(Baris,Kolom1,A):
    os.system('cls')
    print(f'\033[34m<<ISI MATRIKS A BERORDO {Baris} x {Kolom1} >>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            print(A[i][j],end='     ')
        print()

#subrutin mengisi elemen matriks A berordo baris x kolom
def IsiMatriks1(Baris,Kolom1,A):
    print(f'\033[34m<<PENGISIAN MATRIKS A BERORDO {Baris} x {Kolom1} >>\033[30m')
    for i in range(Baris):
        for j in range(Kolom1):
            A[i][j] = int(input('A[{},{}] = '.format(i+1,j+1)))
        print()

#subrutin mengubah matriks A menjadi matriks transpose
def TransposeA(Baris,Kolom1,A,ATranspose):
    for i in range(Baris):
        for j in range(Kolom1):
            ATranspose[j][i] = A[i][j]

#subrutin menampilkan matriks transpose
def TampilTranspose(Baris,Kolom1,A,ATranspose):
    os.system('cls')
    print(f'\033[34m<<MATRIKS TRANSPOSE A BERORDO {Kolom1} x {Baris} >>\033[30m')
    for i in range(Kolom1):
        for j in range(Baris):
            print(ATranspose[i][j],end='     ')
        print()

#badan program utama
os.system('cls')
A = [0] * MAKSBARIS
ATranspose = [0] * MAKSKOLOM1
PenciptaanMatriks1(A,ATranspose)
TampilMatriks(MAKSBARIS,MAKSKOLOM1,A)
print()
os.system('pause')

os.system('cls')
#memasukam banyaknya baris dan kolom
Baris = int(input('Banyak Baris = '))
#validasi baris

#validsi kolom
Kolom1 = int(input('Banyak Kolom = '))

os.system('cls')
IsiMatriks1(Baris,Kolom1,A)
TampilMatriks(Baris,Kolom1,A)
print()
os.system('pause')

os.system('cls')
TransposeA(Baris,Kolom1,A,ATranspose)
TampilTranspose(Baris,Kolom1,A,ATranspose)
print()
os.system('pause')