# width and multiline

# string standar
nama = "udin"
umur = 19
alamat = "jl. damanhuri"
data = "nama {}, umur {}, alamat {}".format(nama, umur, alamat)
center = "BIODATA".center(20, "-")
print(center)
print(data)

# string multiline
nama = "udin"
umur = 19
alamat = "jl. damanhuri"
data = "nama {} \numur {} \nalamat {}".format(nama, umur, alamat)
center = "BIODATA".center(20, "-")
print(center)
print(data)

# string multiline (kutip tiga)
nama = "udin"
umur = 19
alamat = "jl. damanhuri"
data = """
nama: {}
umur: {}
alamat: {}
""".format(nama, umur, alamat)
center = "BIODATA".center(20, "-")
print(center)
print(data)

# mengatur width (lebar)
nama = "udin"
umur = 19
alamat = "jl. damanhuri"
data = """
nama  : {:>10}  # (:>10) --> artinya supaya teksnya bergeser ke arah kanan
umur  : {}
alamat: {}
""".format(nama, umur, alamat)
center = "BIODATA".center(20, "-")
print(center)
print(data)