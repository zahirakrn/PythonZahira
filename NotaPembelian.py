#Program Nota Pembelian
#{I.S.: pengguna memasukan no transaksi, tanggal, dan ketiga data barang  yang 
# dibeli terdiri dari kode barang (KodeBrg) nama barang (NamaBrg), jumlah yang dibeli dan harga satuan setiap barang}
#{F.S.: menampilkan nota pembelian untuk seorang pelanggan}

import os

#badan program
os.system('cls')
#memasukan no transaksi dan tanggal pembelian
NoTransaksi = str(input('No. Transaksi   :')).upper();
Tanggal = str(input('Tanggal     :'))

#memasukan data barang kesatu
print()
print('<< DATA BARANG KESATU >>')
KodeBrg1 = str(input('Kode Barang    :')).upper();
NamaBrg1 = str(input('Nama Barang    :')).upper();
JumlahBeli1 = int(input('Jumlah Beli    :'))
HargaSatuan1 = int(input('Harga Satuan   : Rp. '))
HargaTotal1 = JumlahBeli1 * HargaSatuan1
print(f'Harga Total    : Rp. {HargaTotal1:,.1f}')

#memasukan data barang kedua
print()
print('<< DATA BARANG KEDUA >>')
KodeBrg2 = str(input('Kode Barang    :')).upper();
NamaBrg2 = str(input('Nama Barang    :')).upper();
JumlahBeli2 = int(input('Jumlah Beli    :'))
HargaSatuan2 = int(input('Harga Satuan   : Rp. '))
HargaTotal2 = JumlahBeli2 * HargaSatuan2
print(f'Harga Total    : Rp. {HargaTotal2:,.1f}')

#memasukan data barang ketiga
print()
print('<< DATA BARANG KETIGA >>')
KodeBrg3 = str(input('Kode Barang    :')).upper();
NamaBrg3 = str(input('Nama Barang    :')).upper();
JumlahBeli3 = int(input('Jumlah Beli    :'))
HargaSatuan3 = int(input('Harga Satuan   : Rp. '))
HargaTotal3 = JumlahBeli3 * HargaSatuan3
print(f'Harga Total    : Rp. {HargaTotal3:,.1f}')

print()
os.system('pause')

#membuat tabel nota pembelian
os.system('cls')
print('                         NOTA PEMBELIAN')
print('                         --------------')
print(f'No. Transaksi   : {NoTransaksi:5}                                  Tanggal {Tanggal:10}')
print('--------------------------------------------------------------------------')
print('| Kode Barang |    Nama Barang    | Jumlah | Harga Satuan | Harga Total |')
print('--------------------------------------------------------------------------')
print(f'| {KodeBrg1:11} | {NamaBrg1:17} | {JumlahBeli1:6} | Rp.  {HargaSatuan1:8,} | Rp.  {HargaTotal1:9,.1f} |')
print(f'| {KodeBrg2:11} | {NamaBrg2:17} | {JumlahBeli2:6} | Rp.  {HargaSatuan2:8,} | Rp.  {HargaTotal2:9,.1f} |')
print(f'| {KodeBrg3:11} | {NamaBrg3:17} | {JumlahBeli3:6} | Rp.  {HargaSatuan3:8,} | Rp.  {HargaTotal3:9,.1f} |')
print('=-------------------------------------------------------------------------')


#menghitung total pembelian
TotalPembelian = HargaTotal1 + HargaTotal2 + HargaTotal3
print(f'\nTotal Pembelian : Rp. {TotalPembelian:,.1f}')