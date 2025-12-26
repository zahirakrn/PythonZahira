#Program Menghitung Hitung Volume Tabung
#{I.S.: pengguna memasukan diameter dan tinggi tabung dalam satuan sentimeter}
#{F.S.: menampilkan hasil volume tabung dalam satuan meter kubik}
import os

#konstanta harga Phi
PHI =3.14


#badan program  
os.system('cls')
diameter = float(input('Diameter Tabung (cm) = '))
tinggi = float(input('Tinggi Tabung (cm)   = '))
volumeTabung = (PHI * diameter **2)/4 * tinggi* 0.000001
print(f'Volume Tabung = {volumeTabung:.7f} m3')
