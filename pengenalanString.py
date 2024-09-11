data = "string"
print(data, type(data))

# 1. cara membuat string

'''
    1. membuat string dengan menggunakan single quote '...'
    2. membuat string dengan menggunakan double quote "..."
'''

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('hari jum\'at')

# backslash
print("C:\Home\Python")

# tab \t
print("nama\tsaya")

# backspace \b
print("nama \bsaya")

# newline \n, \r, \r\n
print("baris satu\nbaris dua")  # LF -> line feed -> unix, macos, linux
print("baris satu\rbaris dua")  # CR -> carriage return -> commodore, acorn, lisp
print("baris satu\r\nbaris dua")    # CRLF -> line feed carriage return -> dipakai windows

# 3. string literal atau raw

print("C:\new folder")  # akan salah pathnya

# menggunakan raw string, menggunakan r sebelum tanda petik
print(r"C:\new folder")

# multiline literal string
print("""
nama: Muhammad Firly Al Faridzi
kelas: XII
jurusan: PPLG
 """)

# multiline string dan raw
print(r"""
C:\new folder
D:\new folder
E:\new folder
 """)

print(">>OPERASI DAN MANIPULASI STRING<<\n")

# OPERASI DAN MANIPULASI STRING

# 1. menyambung string (concatenate)
namaPertama = "udin"
namaKedua = "asep"
namaKetiga = "ucup"

nama = namaPertama + " " + namaKedua + " " + namaKetiga
print(nama)

# 2. menghitung panjang string
panjang = len(nama)
print(panjang)

# 3. operator string

# mengecek apakah ada komponen char atau string di dalam string menggunakan in

cek = "adin"
status = cek in nama  # ini cara menggunakannya
print(status)

cek = "lala"
status = cek not in nama  # mengecek bahwa lala tidak ada pada nama maka hasilnya true, jadi jika ada akan false dan jika tidak ada akan true
print(status)

# mengulang string
print("ha"*10)  # cara menggunakannya, dengan menggunakan *(berapa jumlah yang di ingikan)

# indexing
print("index ke-1: ", nama[1])
print("index ke-[0:4]: ", nama[0:4])  # untuk mengambil range array menggunakan (:)
print("index ke-[0,2,4,6,8,10]: ", nama[0:11:2])  # untuk mengambil range array tapi dengan satu satu, menggunakan (:2) artinya increment

# item paling kecil
print("item paling kecil: ", min(nama))  # cara menggunakannya, menggunakan min()

# item paling besar
print("item paling kecil: ", max(nama))  # cara menggunakannya, menggunakan max()

'''

ASCII (American Standard Code for Information Interchange) adalah standar
pengkodean karakter yang digunakan untuk merepresentasikan teks dalam komputer 
dan perangkat elektronik. ASCII menggunakan angka 7-bit untuk merepresentasikan 
karakter, dengan total 128 karakter, termasuk huruf alfabet (baik huruf besar maupun kecil), 
angka, tanda baca, dan karakter kontrol (seperti newline atau tab).

Contoh ASCII code:

Huruf besar "A" diwakili oleh angka 65.
Huruf kecil "a" diwakili oleh angka 97.
Angka "0" diwakili oleh angka 48.
Tanda spasi diwakili oleh angka 32.
ASCII menjadi dasar banyak sistem pengkodean karakter lainnya.

'''

ascii_code = ord(" ")
print("ASCII code spasi adalah: ", str(ascii_code))

data = 100
print("ASCII code 100 adalah: ", chr(data))

print("\n\n")

# 4. operator dalam bentuk method

data = "muhammad firly al faridzi"
jumlah = data.count("l")  # .count(), merupakan method, dan cara menggunakannya
print("jumlah huruf l pada ", data, " adalah ", str(jumlah), "\n")

# merubah case dari string

# merubah semua ke upper case
data = "firly"
print("normal: ", data)
data = data.upper()
print("uppercase: ", data, "\n")

# merubah semua ke lower case
data = "FIRLY"
print("normal: ", data)
data = data.lower()
print("lowercase: ", data, "\n")

# pengecekkan dengan menggunakan isX method

# contoh pengecekan lower case
data = "firly"
cek = data.islower()  # untuk mengecek apakah datanya lower semua, cara menggunakannya
print(data, "is lower: ", cek)

data = "FIRLY"
cek = data.islower()  # untuk mengecek apakah datanya lower semua, cara menggunakannya
print(data, "is lower: ", cek, "\n")

# contoh pengecekan upper case
data = "firly"
cek = data.isupper()  # untuk mengecek apakah datanya upper semua, cara menggunakannya
print(data, "is upper: ", cek)

data = "FIRLY"
cek = data.isupper()
print(data, "is upper: ", cek, "\n")

# isalpha() --> untuk mengecek apakah datanya isinya huruf semua atau tidak, cara menggunakannya

data = "firly"
cek = data.isalpha()  # untuk mengecek apakah semuanya huruf, cara menggunaknnya
print(data, "is alpha: ", cek)

data = "firly12"
cek = data.isalpha()  # untuk mengecek apakah semuanya huruf, cara menggunaknnya
print(data, "is alpha: ", cek, "\n")

# isnumeric() --> digunakan untuk mengecek apakah datanya semuanya angka atau tidak

data = "123"
cek = data.isnumeric()  # untuk mengecek apakah semuanya angka, cara menggunaknnya
print(data, "is numeric: ", cek)

data = "firly123"
cek = data.isnumeric()  # untuk mengecek apakah semuanya angka, cara menggunaknnya
print(data, "is numeric: ", cek, "\n")

# isalnum() --> digunakan untuk mengecek huruf dan angka

data = "firly11"
cek = data.isalnum()  # untuk mengecek apakah angka dan huruf, cara menggunakannya
print(data, "is alnum: ", cek)

data = "firly.11"
cek = data.isalnum()  # untuk mengecek apakah angka dan huruf, cara menggunakannya
print(data, "is alnum: ", cek, "\n")

# isspace() --> digunakan untuk mengecek apakah datanya memiliki spasi, tab, newline

data = "firly al faridzi"
cek = data.isspace()
print(data, "is space: ", cek, "\n")

# istitle() --> digunakan untuk mengecek apakah awal katanya menggunakan huruf besar

data = "firly"
cek = data.istitle()  # untuk mengecek apakah huruf pertama menggunakan kapital, cara menggunakannya
print(data, "is title: ", cek)

data = "Firly"
cek = data.istitle()  # untuk mengecek apakah huruf pertama menggunakan kapital, cara menggunakannya
print(data, "is title: ", cek, "\n")

# mengecek komponen, startswith() dan endswith()

cek_start = "firly".startswith("firly")
print("startswith: ", cek_start)

cek_end = "firly".endswith("firly")
print("endswith: ", cek_end, "\n")

# penggabungan komponen, join() dan split()

pisah = ['hello', 'world']
gabung = ' '.join(pisah)  # digunakan untuk menggabungkan data yang terpisah, cara menggunakannya
print("join: ", gabung)

gabung = "hellotesworld"
print("split: ", gabung.split("tes"), "\n")  # digunakan untuk memisahkan data yang tergabung, cara menggunakannya

# alokasi karakter, rjust(), ljust, center()

rjust = "kanan".rjust(10, "-")
print("rjust: ", rjust)  # digunakan untuk mengatur agar datanya berada di sebalah kanan

ljust = "kiri".ljust(10, "-")
print("ljust: ", ljust)  # digunakan untuk mengatur agar datanya berada di sebelah kiri

center = "tengah".center(20, "-")
print("center: ", center, "\n")  # digunakan untuk mengatur datanya berada di tengah

# kebalikannya menggunakan strip()

center = center.strip("-")  # digunakan untuk menghilagkan tanda(-) yang ada pada center
print("strip: ", center)

rjust = rjust.strip("-")  # digunakan untuk menghilagkan tanda(-) yang ada pada rjust
print("strip: ", rjust)

ljust = ljust.strip("-")
print("strip: ", ljust)  # digunakan untuk menghilagkan tanda(-) yang ada pada ljust