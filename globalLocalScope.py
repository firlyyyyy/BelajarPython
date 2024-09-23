""" GLOBAL AND LOCAL SCOPE """

# global scope
nama_global = 'ucup'  # variable global

# akses variable global menggunakan fungsi
def fungsi1():
    print(f"nama dia (fungsi) {nama_global}")
    
fungsi1()

# akses variable global menggunakan loop
for i in range(5):
    print(f"nama dia (loop) {nama_global}")
    
# akses variable global menggunakan if
if True:
    print(f"nama dia (if) {nama_global}")
    
# local scope
def fungsi2():
    nama_local = 'dudung'  # variable local
    
""" CONTOH PENGGUNAAN VARIABLE LOCAL """
# contoh 1: penggunaan akses variable
def hai():
    print(f"hai {nama}")
nama = 'udin'
hai()

# contoh 2: cara merubah nilai variable global
angka = 0
nama = 'ceko'

def ubah(nilaiBaru, namaBaru):
    global angka  # fungsi ini mendapat akases merubah angka
    global nama
    nama = namaBaru
    angka = nilaiBaru
print(f"sebelum dirubah = {angka, nama}")
ubah(10, 'celos')
print(f"sesudah dirubah = {angka, nama}")

# contoh 3
angka = 0

for i in range(10):
    angka += 1
    angka_dumy = 0
print(angka)
print(angka_dumy)

if True:
    angka = 20
    angka_dumy = 30
print(angka)
print(angka_dumy)