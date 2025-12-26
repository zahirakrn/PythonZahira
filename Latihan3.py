#Program Menghitung Hitung Luas Persegi Panjang
#{I.S. : pengguna memasukan panjang dan lebar persegi panjang}
#{F.S. : menampilkan hasil luas persegi panjang}
import os

#badan program
os.system('cls')
panjang = float(input('Masukan Panjang = '))
lebar = float(input('Masukan Lebar = '))
luasPersegi = panjang * lebar
print(f'Luas Persegi Panjang = {panjang:.0f} * {lebar:.0f}')
print(f' = {luasPersegi:.1f}')
