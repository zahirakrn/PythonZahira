#Program Menentukan Genap Ganjil
#I.S. : pengguna memasukkan sebuah bilangan
#F.S. : menampilkan keterangan "Bilangan Genap" atau "Bilangan Ganjil"

import os

#badan program
os.system('cls')
'''
#analisis terhadap satu kasus
Bilangan = int(input('Memasukan sebuah bilangan : '))
Keterangan = 'Bilangan Ganjil'
if (Bilangan % 2 == 0):
    Keterangan = 'Bilangan Genap'

print(f'{Bilangan} adalah {Keterangan}')
'''

#analisis terhadap satu kasus
Bilangan = int(input('Memasukan sebuah bilangan : '))

if (Bilangan % 2 == 0):
    Keterangan = 'Bilangan Genap'
else:
    Keterangan = 'Bilangan Ganjil'
print(f'{Bilangan} adalah {Keterangan}')