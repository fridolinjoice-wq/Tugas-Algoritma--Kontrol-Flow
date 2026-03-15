##Introduction##

#Contoh Penerapan Library Python
# 1. Library requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

# 2. Library Math
import math

print(math.sqrt(16))
print(math.pi)

# 3. Library random
import random

angka = random.randint(1, 10)
print("Angka acak:", angka)

# 4. Library datetime
from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

#Studi Kasus Sederhana
import random

nilai = random.randint(50, 100)
print("Nilai:", nilai)

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")


print("---------------")

##Komponen Utama Conditional Statements##
# 1. Types of Conditional Statements:
nilai = 85
if nilai >= 90:
    print("Grade: A")
elif nilai >= 80:
    print("Grade: B+")
else:
    print("Grade: C")
print("---------------")

number = 6
if number > 5:
    # Calculate square
    print(number * number)
print('Next lines of code')


# 2. If – else statement
password = input('Enter password ')
if password == "PYnative@#29":
    print("Correct password")
else:
    print("Incorrect Password")

#Syntax of the if-elif-else statement:
def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")
user_check(1)
user_check(2)
user_check(3)
user_check(4)


# 3. Menggunakan Input dari Pengguna
x = int(input("Masukkan nilai x: "))
if x > 5:
    print("x lebih besar dari 5")
elif x == 5:
    print("x sama dengan 5")
else:
    print("x lebih kecil dari 5")


# 4. Menggunakan if Bersarang (Nested If)
x = int(input("Masukkan nilai x: "))
if x > 0:
    print("x adalah bilangan positif")
    if x % 2 == 0:
        print("x juga bilangan genap")
    else:
        print("x adalah bilangan ganjil")
elif x == 0:
    print("x adalah nol")
else:
    print("x adalah bilangan negatif")

# 5. Menggunakan Operator Logika dalam if
x = int(input("Masukkan nilai x: "))
if x > 0 and x % 2 == 0:
    print("x adalah bilangan positif dan genap")
elif x > 0 and x % 2 != 0:
    print("x adalah bilangan positif dan ganjil")
else:
    print("x bukan bilangan positif")

# 6. Menggunakan Ternary Operator (if dalam satu baris)  
x = int(input("Masukkan nilai x: "))
status = "Positif" if x > 0 else "Negatif atau Nol"
print(f"x adalah bilangan {status}")

# 7. Variabel yang Bisa Digunakan dalam if, elif
#Boolean (bool)
is_active = True
if is_active:
    print("Akun aktif")

#Angka (int, float) (Seperti contoh di atas..)
nilai = 75
if nilai >= 60:
    print("Lulus")
elif nilai < 60:
    print("Tidak Lulus")

#String (str)
nama = "Andi"
if nama:
    print("Nama telah diisi")

#List, Tuple, Set, Dictionary (list, tuple, set, dict)
data = []
if data:
    print("List memiliki isi")
else:
    print("List kosong")

#NoneType (None)
user = None
if user is None:
    print("User belum login")


##Transfer Statements (Pernyataan##
# 1. break Statement
for i in range(10):
    if i == 5:
        break
    print(i)

#2. continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)

#3. pass Statement
def fungsi_belum_jadi():
    pass

#contoh
nilai = 80
if nilai > 75:
    pass
else:
    print("Nilai belum lulus")

# 4. return Statement
def add(a, b):
    return a + b

hasil = add(3, 5)
print(hasil)


hasil = 0

def hitung(a, b):
    global hasil
    hasil = a + b

hitung(4, 6)
print(hasil)

##Perbedaan for dan while##
# Contoh Perbandingan:
# Menggunakan for (jumlah sudah pasti 5 kali)
for i in range(5):
    print("Perulangan ke-", i)

# Menggunakan while
i = 0
while i < 5:
    print("Perulangan ke-", i)
    i += 1

#Kontrol dalam Perulangan
# 1. break
for i in range(10):
    if i == 5:
        break
    print(i)

#2. continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# 3. else pada Loop
for i in range(3):
    print(i)
else:
    print("Loop selesai tanpa break")

#Nested Loop (Perulangan Bersarang)
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

#Aplikasi Iterasi dalam Algoritma
#1. Menghitung Jumlah Total
angka = [10, 20, 30, 40]
total = 0
for nilai in angka:
    total += nilai

print("Total:", total)

#2. Menghitung Faktorial
n = 5
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

#3. Validasi Input dengan while
nilai = -1
while nilai < 0:
    nilai = int(input("Masukkan angka positif: "))

print("Input diterima")

