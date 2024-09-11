# format string

# contoh generic

# string
nama = "udin"
format_str = f"hai nama saya {nama}"  # contoh penggunaan format string, menggunakan huruf f sebelum tanda petik
print(format_str)

# angka
angka = 1999
format_str = f"tahun {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"nilai ini {boolean}"
print(format_str)

# bilangan bulat
bb = 10
format_str = f"bilangan bulat {bb:d}"  # (:d) biar bilangan itu hasilnya int bukan float, opsional, bisa pakai atau tidak
print(format_str)


# bilangan dengan ordo ribuan
angka = 5000
format_str = f"uang Rp. {angka:,}"  # (:,) digunakan untuk memunculkan koma pada bilangan dengan ordo ribuan
print(format_str)

# bilangan desimal
angka = 199.999
format_str = f"nilai desimal {angka:.2f}"  # (:.2f) --> artinya mengambil 2 angka di belakang koma, dan f itu tipe data yang dipakai, jika angka 199.999 maka akan di bulatkan menjadi 200.00
print(format_str)

# menampilka leading zero
angka = 878.672
format_str = f"leadind zero {angka:07.2f}"  # (:07.2) --> artinya 07 akan memberikan 0 di depan angka, dan mengambil 2 di belakang koma
print(format_str)

# menampilan tanda + dan -
angkaMinus = -12
angkaPlus = 12.781
formatMinus = f"minus {angkaMinus:+d}"  # (:+d) --> artinya akan menampilan plus ataupun minus
formatPlus = f"plus {angkaPlus:+.2f}"  # (:+d) --> artinya akan menampilan plus ataupun minus, note: juga bisa menggunakan (:+.2f), tidak usah menggunakan (d)
print(formatMinus)
print(formatPlus)

# format persen
angkaPersen = 0.017
formatPersen = f"persen {angkaPersen:.2%}"  # (:.2%) --> artinya akan membuat angka menjadi persen dan mengambil 2 angka di belakang titik
print(formatPersen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 6
format_str = f"harga {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 199
formatBinary = f"binary {bin(angka)}"
formatOctal = f"octal {oct(angka)}"
formatHex = f"hex {hex(angka)}"
print(formatBinary)
print(formatOctal)
print(formatHex)

# menggunakan str.format
nama = "udin"
umur = "19"
alamat = "jl.damanhuri"
namaPanjang = "udinnnnn"
format_str = "nama saya {} umur saya {} tahun, rumah saya di {}, nama panjang saya {}".format(nama, umur, alamat, namaPanjang)
print(format_str)