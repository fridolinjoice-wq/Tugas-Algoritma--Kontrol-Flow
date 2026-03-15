#Deklarasi Variabel
a = "** Bisnis Digital feb unm **" # string
print(a)
print('---------------')

#Multiple variables
x, y, z = "Aku", " Bisa", "  Python"
print(x)
print(y)
print(z)
print('---------------')

#Re-declaration of variables
a = "aku bisa"
print(a+z)

print(x,y,z)
print('---------------')
x, y, z, = "Aku", "PASTI BISA", "Python"
print(x,y,z)
print('a.',x, 'b.',y, 'p.',z, type(x))
print('---------------')

#4. Variabel dan tipe data
panjang = 5
lebar = 5.5
luas = panjang * lebar
print('luas:', panjang, '*', lebar, '=', luas)
print("Tipe dari variabel panjang:", type(panjang))
print(" Tipe dari variabel lebar:",)
print(" Tipe dari variabel luas:", type(luas))
print('---------------')

#5. Variabel dengan f-string
nama = 'olin'
umur = 17
ipk = 3.76
print(f"Halo, nama saya {nama}, umur saya {umur} tahun, dan IPK saya {ipk}.")
print('---------------')





#Global dan Lokal Variable
#1. This function is using local variable
def fun ( ):
    umur = 17
    print ('umur:', umur)
fun ( )
print('---------------')

#2. Fungsi
x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is "+ x)
myfunc()

print("python is " + x)
print('---------------')

#3. Operasi string
var1 = 'princess'
var2 = 'fridolin'
var3 = 'joice'
var3 = (var1+var2)
print(var3)
print('---------------')

#4. Menampilkan input di user
nama = input("ketik nama anda: ")
nim = int(input("ketik nim: "))
print("Salam !," + nama, + nim,)
print('---------------')

#5. multiple inputs from the user dengan : split() method.
a, b = input('Masukkan dua integer: ').split()
print("a =",a, ",b = ",b)
print("---------------")

#6. Multiple inputs from the user dengan : split() method.
nama, umur, alt = input("input identitas nama, umur, alamat: ").split()
print("nama:", nama)
print("umur:", umur)
print("alamat:", alt)
print('---------------')

#Struktur Data Types
#1. Membuat list 
#list kosong
list_kosong = []
#list bernilai string
list1 = ['aku', 'selalu', 'bahagia']
#list bernilai integer
list2 = [10, 20, 30,40]
#list campuran
list3 = [15, 33.33, 'bisdig', False]
print(list_kosong)
print(list1)
print(list2)
print(list3)
print('---------------')

#2. Contoh indeks
list1 = ['p', 'Y', 'T', 'H', 'O', 'N']
list3 = [15, 33.33, 'bisdig', False]

print(list1[0], ':adalah indeks.0')
print(list1[-3], ':adalah indeks.-3')

print(list1[0:3])
print(list1[0:1])
print(list1[0:2])
print(list1[1:3])
print(list1[0:-1])
print(list1[-3:-1])
print('---------------')

print(list1[0:])
print(list1[1:])
print(list1[2:])
print(list1[3:])
print(list1[:0])
print(list1[:1])
print(list1[:2])
print(list1[:3])
print(list1[:4])

#3. Contoh list method
a=[1,2,3,4,5]
b=[7,8,9]
#a.append(6), add element pada list lain
a.append('6')
print(a)
#a.insert(index, element), insert elemen pada index yang ditentukan
a.insert(0,0)
#a.extend(b)
a.extend(b)
print('---------------')

#4. Advanced list
#Membuat list kuadrat
A =[x**2 for x in range(1,9)]
print(A)

B =[x for x in range(1,10) if x%2==0]
print(B)
print('---------------')

#5. Contoh tuple
tup1 = ('olin', 'data', 2020, 2021)
tup2 = (10, 20, 30, 40, 50 )
tup3 = "A", "B", "C", "D"
print(tup1,tup2,tup3)
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print('---------------')

#6. Dictionary pada python
dict = {'Name': 'Olin', 'Age': 17, 'Class': 'A'}
print ("dict['Name]: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print('---------------')

#7. Update dictionary python
dict = {'Name': 'Olin', 'Age': 17, 'Class': 'A'}
dict['Age'] = 17; # Mengubah entri yang sudah ada
dict['University'] = "UNM" # Menambah entri baru
print ("dict['Age']: ", dict['Age'])
print ("dict['University']: ", dict['University'])
print('---------------')

#8. Menghapus data dictionary
dict = {'Name': 'Olin', 'Age': 17, 'Class': 'A'}
del dict['Name'] # hapus entri dengan key 'Name'
dict.clear() # hapus semua entri di dict
del dict # hapus dictionary yang sudah ada
print ("dict['Age]: ", dict['Age'])
print ("dict['University']: ", dict['University'])