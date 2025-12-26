#Program Fotokopi Susah Gampang
#I.S.: pengguna memasukkan status konsumen(Langganan[Y/T]), tanggal transaksi(Tanggal), jumlah fotokopi(Jumlah)
#F.S.: menampilkan harga per lembar(Harga) dan total uang yang harus dibayar oleh konsumen (TotalBayar)
import os

#badan program
os.system('cls')
Tanggal = str(input('Tanggal Transaksi      : '))
Langganan = str(input('Status Langganan [Y/T] : ')).upper()
#validasi status konsumen
if Langganan != "Y" and Langganan != "T":
    print('Status Langganan bisa diisi Y atau T')
else:
    Jumlah = int(input('Jumlah fotokopi        : '))
    #menentukan harga per lembar
    match(Langganan):
        case "Y":
            Harga = 200
        case "T":
            if Jumlah < 100:
                Harga = 300
            else:
                Harga = 250
    #menghitung total harga yang harus dibayar
    TotalBayar = Jumlah * Harga
    #menampilkan harga per lembar dan total harga yang harus dibayar
    print(f'Harga Per lembar       : Rp. {Harga:,}')
    print(f'Total Bayar            : Rp. {TotalBayar:,}')