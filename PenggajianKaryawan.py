#Program Penggajian PT. Ceria Selalu
#I.S.: pengguna memasukan bulan dan tahun penggajian, beserta nomor induk karyawan (NIK), nama karyawan (Nama)
#      golongan (Gol), dan jam kerja satu bulan (JamKerja)
#F.S.: menampilkan slip gaji yang diterima seorang karyawan

import os

#badan program
os.system('cls')
print('\033[33m<<Data Penggajian Karyawan>>')
print('-------------------------------\033[0m')
print()
Bulan = str(input('Bulan Penggajian       : ')).upper()
Tahun = str(input('Tahun Penggajian       : '))
NIK = str(input('Nomor Induk Karyawan   : ')).upper()
Nama = str(input('Nama Karyawan          : ')).upper()
Gol = int(input('Golongan               : '))
JamKerja = int(input('Jumlah Jam Kerja/Bulan : '))
Status = str(input('Status Pernikahan      :')).upper()
if(Status == 'M'):
    Anak = int(input('Jumlah Anak            : '))
else:
    Anak = 0

#menentukan gaji pokok dan tunjangan
if(Gol ==1):
    GajiPokok = 1750000
    BesarTunjangan = '12,5%'
    Tunjangan = 0.125 * GajiPokok
else:
    GajiPokok = 2300000
    BesarTunjangan = '15%'
    Tunjangan = 0.15 * GajiPokok

#menghitung tunjangan anak
TunjanganAnak = Anak *(0.075 * GajiPokok)
if (Anak > 2):
    TunjanganAnak = 2 *(0.075 * GajiPokok)

#menghitung  jam lembur dan uang lembur
JamLembur = 0
UangLembur = 0 
if (JamKerja > 208):
   JamLembur = JamKerja - 208
   UangLembur = JamLembur * 250000

#menghitung jam kurang
JamKurang = 0 
if (JamKerja < 208):
    JamKurang = 208 - JamKerja


#menghitung uang potong
if (JamKurang >= 8):
    Hari = JamKurang // 8
    Sisa = JamKurang % 8
    UangPotongan = Hari * 50000 + Sisa * 10000
else:
    UangPotongan = JamKurang * 10000

#menghitung gaji bersih
GajiBersih = GajiPokok + Tunjangan + TunjanganAnak + UangLembur - UangPotongan

#menghitung slip gaji
os.system('cls')
print('                     \033[33m<<SLIP GAJI>>')
print('                     -------------\033[0m')
print()
print(f'\033[34mBulan : {Bulan:10}   Tahun : {Tahun:>20}')
print(f'NIK   : {NIK:10}    Nama : {Nama:>20}\033[0m')
print('\033[33m--------------------------------------------------\033[0m')
print(f'Golongan                    : {Gol}')
print(f'Jumlah Jam Kerja/Bulan      : {JamKerja} Jam')
print(f'Gaji Pokok                  : Rp.  {GajiPokok:10,}')
print(f'Tunjangan  {BesarTunjangan:5}            : Rp. {Tunjangan:12,.1f}')
print(f'Tunjangan Anak              : Rp. {TunjanganAnak:12,.1f}')
if (JamLembur > 0):
    print(f'Lembur                      : \033[31m{JamLembur}\033[0m \033[34mJam')
    print(f'                            : Rp.  {UangLembur:10,}')
else:
     print(f'Lembur                      : Rp.  {UangLembur:10,}')
if (JamKurang > 0):
    print(f'Potongan                   : \033[31m-{JamKurang}\033[0m \033[34mJam')
    print(f'                           : Rp.  {UangPotongan:10,}')
else:
     print(f'Potongan                    : Rp.  {UangPotongan:10,}')
print('\033[33m--------------------------------------------------\033[0m')
print(f'\033[34mGaji Bersih                 : Rp. \033[0m\033[31m{GajiBersih:12,.1f}\033[0m')

