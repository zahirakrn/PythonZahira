#Program Mengubah Infix Menjadi Postfix (Linked List)
#I.S.: pengguna memasukkan sebuah ekspresi dalam notasi infix(E)
#F.S.: menampilkan hasil postfix dan hasil perhitungan dalam keadaan postfix

import os

#konstanta maksimal simbol
MAKSSIMBOL = 30

#pendefinisian kelas

#0. kelas node
class Node:
    #method inisialisasi node
    def __init__(self,Info):
        self.Info = Info
        self.Next = None


#1. kelas stack linked list
class StackLinked:
    #method inisialisasi
    def __init__(self):
        self.Top = None

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top is None

    #method menambah satu data ke dalam stack (Push)
    def Push(self,Info):
        Baru = Node(Info)
        Baru.Next = self.Top
        self.Top = Baru

    #method mengeluarkan satu data dari stack (Pop)
    def Pop(self):
        if not self.Kosong():
            Hapus = self.Top
            self.Top = self.Top.Next
            return Hapus.Info
        return None

    #method mengambil isi teratas stack
    def Peek(self):
        if not self.Kosong():
            return self.Top.Info
        return None


#2. kelas untuk mengubah infix menjadi postfix
class InfixToPostfix:

    #method inisialisasi
    def __init__(self):
        self.Stack = StackLinked()
        self.Q = [' '] * MAKSSIMBOL
        self.P = [' '] * MAKSSIMBOL
        self.Operator = set(['+','-','*','/','^'])

    #method tingkat operator
    def TingkatOpr(self,Opr):
        if (Opr == '+') or (Opr == '-'):
            return 1
        elif (Opr == '*') or (Opr == '/'):
            return 2
        else:
            return 3

    #method mengubah infix menjadi postfix
    def Postfix(self,N):

        #push kurung buka ke dalam stack
        self.Stack.Push('(')

        #tambahkan kurung tutup di sentinel Q
        self.Q[N] = ')'

        #pindai simbol di Q dari kiri ke kanan sampai stack kosong
        i = 0
        j = 0

        while(not self.Stack.Kosong()):

            #jika yang dipindai operand
            if (self.Q[i] not in self.Operator) and \
               (self.Q[i] != '(') and \
               (self.Q[i] != ')'):

                #tambahkan ke postfix
                self.P[j] = self.Q[i]
                j += 1

            #jika yang dipindai kurung buka
            elif(self.Q[i] == '('):

                #push ke stack
                self.Stack.Push('(')

            #jika yang dipindai operator
            elif(self.Q[i] in self.Operator):

                #cek prioritas operator
                while(not self.Stack.Kosong()) and \
                     (self.Stack.Peek() in self.Operator) and \
                     (self.TingkatOpr(self.Stack.Peek()) >= self.TingkatOpr(self.Q[i])):

                    #pop dari stack lalu masukkan ke postfix
                    self.P[j] = self.Stack.Peek()
                    j += 1
                    self.Stack.Pop()

                #push operator yang dipindai
                self.Stack.Push(self.Q[i])

            #jika yang dipindai kurung tutup
            else:

                #pop sampai bertemu kurung buka
                while(self.Stack.Peek() != '('):

                    self.P[j] = self.Stack.Peek()
                    j += 1
                    self.Stack.Pop()

                #hapus kurung buka
                self.Stack.Pop()

            i += 1

        return j

    #method menampilkan postfix
    def TampilPostfix(self,N):

        print('P : ',end='')

        for j in range(N):
            print(self.P[j],end='')

            if(j < N-1):
                print(', ',end='')

        print()


#3. kelas untuk menghitung dalam keadaan postfix
class HitungPostfix:

    #method inisialisasi
    def __init__(self):
        self.Stack = StackLinked()
        self.Operator = set(['+','-','*','/','^'])

    #method menghitung postfix
    def Hitung(self,P,N):

        #tambahkan sentinel
        P[N] = ')'

        #pindai postfix dari kiri ke kanan
        j = 0

        while(P[j] != ')'):

            #jika operand
            if(P[j] not in self.Operator):

                #push ke stack
                self.Stack.Push(P[j])

            #jika operator
            else:

                #ambil dua operand dari stack
                A = int(self.Stack.Pop())
                B = int(self.Stack.Pop())

                #lakukan operasi
                match(P[j]):
                    case '+':
                        Hasil = B + A

                    case '-':
                        Hasil = B - A

                    case '*':
                        Hasil = B * A

                    case '/':
                        Hasil = B / A

                    case '^':
                        Hasil = B ** A

                #push hasil ke stack
                self.Stack.Push(Hasil)

            j += 1

        #ambil hasil akhir
        Value = self.Stack.Pop()

        #tampilkan hasil
        print(f'Value = {Value}')


#badan program utama
os.system('cls')

Notasi = InfixToPostfix()

#pengguna memasukkan ekspresi infix
print('<-- PROGRAM MENGUBAH INFIX MENJADI POSTFIX -->')
E = str(input('Ekspresi Infix (E) = '))

#memasukkan ekspresi E ke array Q
print('Q : ',end='')

j = 0

for i in range(len(E)):

    if(E[i] != ' '):

        Notasi.Q[j] = E[i]
        print(Notasi.Q[j],end=' ')
        j += 1

N = j

#memanggil method mengubah infix menjadi postfix
N = Notasi.Postfix(N)

print()

Notasi.TampilPostfix(N)

#memanggil method menghitung postfix
Hitung_Postfix = HitungPostfix()
Hitung_Postfix.Hitung(Notasi.P,N)