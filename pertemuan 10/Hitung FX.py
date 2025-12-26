#Program Menghitung FX
#I.S.: pengguna memasukan harga X
#F.S.: menampilkan hasil perhitungan F(X) = 2X + 1
import os

#subrutin memasukan harga x
def IsiX(X):
    X = int(input('Masukan Harga X = '))
    return X

#subrutin menghitung F(X)
def F(X):
    return 2 * X + 1

#subrutin menampilkan hasil perhitungan F(X) = 2X + 1
def TampilFX(X):
    print(f'F({X:2}) = 2 x {X} + 1')
    print(f'      = {F(X)}')


#badan program utama
os.system('cls')
X = 0
X = IsiX(X)
TampilFX(X)
