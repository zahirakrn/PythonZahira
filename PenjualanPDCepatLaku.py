#Program Penjualan PD Cepat Laku
#I.S. : pengguna memasukan kode barang (KodeBrg), jumlah yang dibeli (jumlah)

#F.S. : menampilkan total harga yang harius dibayar oleh seorang pembeli beserta uang kembalian
import os

#badan program
os.system('cls')
print('\033[33m<<DATA PENJUALAN BARANG >>\033[0m')
KodeBrg = str(input('Kode Barang           : ')).upper()
#validasi kode barang
if (KodeBrg !='PK01') and (KodeBrg !='TS02') (KodeBrg !='SP03') (KodeBrg !='AK04'):
    print('\033[31mkode barang tidak ada!\033[0m')
else:
    Jumlah = int(input('Jumlah Beli           : '))
    #menentukan ada diskon atau tidak
    BesarDiskon = 0
    if (Jumlah >= 10): #tidak kurang dari setengah kodi
        AdaDiskon = str(input('Ada Diskon[Ya/Tidak]  : ')).upper()
        if (AdaDiskon == 'YA'):
            BesarDiskon = float(input('Besar Diskon (%)      : ')) 

    #menentukan nama barang dan harga satuan
    match(KodeBrg):
        case 'PK01':
            NamaBrg = 'Pakaian'
            HargaSatuan = 750000
        case 'TS02':
            NamaBrg = 'Tas'
            HargaSatuan = 655000
        case 'SP03':
            NamaBrg = 'Sepatu'
            HargaSatuan = 157000
        case 'AK04':
            NamaBrg = 'Aksesoris'
            HargaSatuan = 450000

    #menghitung harga total
    HargaTotal = Jumlah * HargaSatuan

    #menghitung potongan
    Potongan = 0 
    if (BesarDiskon > 0):

        Potongan = BesarDiskon/100 * HargaTotal


    #menghitung total bayar
    TotalBayar = HargaTotal - Potongan


    #menghitung nota penjualan
    os.system('cls')
    print('\033[33m**NOTA PENJUALAN BARANG**\033[0m')
    print()
    print(f'Kode Barang      : \033[31m{KodeBrg}\033[0m')
    print(f'Nama Barang      : \033[31m{NamaBrg}\033[0m')
    print(f'Jumlah           : \033[31m{Jumlah}\033[0m pcs')
    print(f'Harga Satuan     : Rp. \033[31m {HargaSatuan:10,}\033[0m')
    print(f'Harga Potongan   : Rp. \033[31m {HargaTotal:10,}\033[0m')
    print(f'Diskon {BesarDiskon} %     : Rp. \033[31m {Potongan:12,.1f}\033[0m')
    print(f'               ----------------------')
    print(f'Total Bayar      : Rp. \033[31m {TotalBayar:12,.1f}\033[0m')

    #memasukan uang pembayaran 
    Bayar = int(input('pembayaran       : Rp.'))
    #mengecek uang pembayaran 
    if (Bayar < TotalBayar):
        print('\033[33mPembayaran Kurang!\033[0m')
        #memasukan uang pembayaran lagi
        Bayar = int(input('Pembayaran     : Rp.  '))

    #menghitung uang kembalian
    Kembalian = Bayar - TotalBayar 
    #menampilkan uang kembalian
    print(f'Kembalian      : Rp. \033[31m {Kembalian:12,.1f}\033[0m')
