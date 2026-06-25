# Program mengubah infix menjadi postfix
# I.S.: pengguna memasukkan ekspresi dalam notasi infix
# F.S.: menampilkan hasil postfix dan hasil perhitungan dalam keadaan postfix
import os

#konstanta maksimal simbol
MAKSSIMBOL = 30

#pendefinisian kelas
#1. Kelas untuk mengubah infix menjadi postfix
class InfixToPostfix:
    #method inisialisasi
    def __init__(self):
        self.Top = -1
        self.Stack = [' '] * MAKSSIMBOL
        self.Q = [' '] * MAKSSIMBOL
        self.P = [' '] * MAKSSIMBOL
        self.Operator = set(['+', '-', '*', '/', '^'])

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top == -1
    
    #method menambah satu data ke dalam stack (push)
    def Push(self,Simbol):
        self.Top += 1
        self.Stack[self.Top] = Simbol    

    #method mengeluarkan data ke dalam stack (pop)
    def Pop(self):
        self.Stack[self.Top] = ' '
        self.Top -= 1

    #method tingkat operator
    def TingkatOpr(self,Opr):
        if(Opr =='+') or (Opr =='-'):
            return 1
        elif(Opr =='*') or (Opr =='/'):
            return 2
        else:
            return 3
        
    #method mengubah infix menjadi postfix
    def Postfix(self,N):
        #push kurung buka kedalam Stack
        self.Push('(')
        #tambahkan kurung tutup kedalam sentinel Q
        self.Q[N] = ')'
        #pindai simbol di Q dari kiri ke kanan sampai stack kosong
        i = 0 # indeks untuk Q
        j = 0   # indeks untuk P
        while (not self.Kosong()):
            #jika yang dipindai adalah operand
            if (self.Q[i] not in self.Operator) and (self.Q[i] != '(') and (self.Q[i] != ')'):
                #tambahkan ke P
                self.P[j] = self.Q[i]
                j += 1
            elif(self.Q[i] == '('): #jika yang dipindai adalah operator atau kurung buka
                #push ke dalam stack 
                self.Push('(')
            elif(self.Q[i] in self.Operator): #jika yang dipindai adalah operator
                #cek isi teratas stack, jika operator dan tibngkatannya sama atau lebih besar dengan operator yang dipindai, maka pop dari stack ke P
                while (self.Stack[self.Top] in self.Operator) and (self.TingkatOpr(self.Stack[self.Top]) >= self.TingkatOpr(self.Q[i])):
                    #pop dari stack lalu tambahkan ke P
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()
                #tambahkan (push) operator yang dipindai ke dalam stack
                self.Push(self.Q[i])
            else : #jika yang dipindai kurung tutup
                #pop dari stack berulangkali sampai kurung buka
                while(self.Stack[self.Top] != '(' ):
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()

                #pop kurung buka dari stack
                self.Pop()
            
            i += 1

        return j

    #method menampilkan hasil postfix
    def TampilPostfix(self,N):
        print('P : ', end=' ')
        for j in range(N):
            print(self.P[j], end =' ')
            if (j < N-1 ):
                print (',', end='')
        
#2. Kelas untuk menghitung dalam keadaan postfix
class HitungPostfix:
    #method inisialisasi
    def __init__(self):
        self.Top = -1
        self.Stack = [' '] * MAKSSIMBOL
        self.Operator = set(['+', '-', '*', '/', '^'])

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top == -1
    
    #method menambah satu data ke dalam stack (push)
    def Push(self,Simbol):
        self.Top += 1
        self.Stack[self.Top] = Simbol   

    #method mengeluarkan data ke dalam stack (pop)
    def Pop(self):
        self.Stack[self.Top] = ' '
        self.Top -= 1

    #method menghitung dalam keadaan Postfix
    def Hitung(self,P,N):
        #tambahkan turung kurung di sentinel P
        P[N]  = ')'
        j = 0
        #pindai simbol P dari kiri ke kanan sampai tanda kurung tutup ditemukan 
        while ( P[j] != ')'):
            #jika yang di pindai operan
            if (P[j] not in self.Operator):
                #push ke dalam stack
                self.Push(P[j])
            else: #jika yang dipindai operator
                #pop dua elemen Stack
                A = int(self.Stack[self.Top])
                self.Pop()
                B = int(self.Stack[self.Top])
                self.Pop()

                #menghitung dengan format B operator A
                match (P[j]):
                    case '+' : Hasil = B + A
                    case '-' : Hasil = B - A
                    case '*' : Hasil = B * A
                    case '/' : Hasil = B / A
                    case '^' : Hasil = B ** A

                #push hasil perhitungan ke dalam stack
                self.Push(Hasil)

            j += 1

        #keluarkan isi stack simpan di var value
        Value = self.Stack[self.Top]
        self.Pop()
        #Tampil isi value
        print(f'Value = {Value}')

#Bagian utama program
os.system('cls')
Notasi = InfixToPostfix()

#Pengguna memasukkan ekspresi dalam notasi infix(E)
print("--> PROGRAM MENGUBAH INFIX MENJADI POSTFIX <--")
E = str(input("Ekspresi infix (E) : "))

#Memasukkan ekspresi E ke dalam Array Q
print('Q : ', end='')
j = 0
for i in range(len(E)):
    if (E[i] != ' '):
        Notasi.Q[j] = E[i]
        print(Notasi.Q[j], end=' ')
        j += 1

N = j

#memanggil method mengubah infix menjadi postfix
N = Notasi.Postfix(N)
print()
Notasi.TampilPostfix(N)

#memanggil method menghitung dalam keadaan postfix
Hitung_Postfix = HitungPostfix()
Hitung_Postfix.Hitung(Notasi.P,N)