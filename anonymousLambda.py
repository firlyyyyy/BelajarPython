""" ANONYMOUS AND LAMBDA """

""" LAMBDA FUNCTION """
# A lambda function is a small anonymous function that can take any number of arguments, but can only
# have one expression.
# Syntax: lambda arguments : expression
# Example:
def double(x): return x * 2


print(double(5))  # Output: 10


def f_kuadrat(angka):
    return angka ** 2


print(f"hasil fungsi kuadrat = {f_kuadrat(5)}")


def kuadrat(angka): return angka**3


print(f"hasil lambda kuadrat = {kuadrat(5)}")


def pangkat(angka, pangkat): return angka**pangkat


print(f"hasil lambda pangkat = {pangkat(5, 2)}")
print("\n")

""" SORTING BIASA """
dataList = ['jjjjj', 'kkkkkk', 'aaaaaaa', 'yyyyyyyyy']
dataList.sort()
print(f"sorted list biasa \t\t= {dataList}")


""" SORTING PAKAI PANJANG MENGGUNAKAN LEN """


def panjang(nama):
    return len(nama)


dataList.sort(key=panjang)
print(f"sorted list by fungsi panjang \t= {dataList}")

dataList.sort(key=len)
print(f"sorted list by len \t\t= {dataList}")

""" SORTING MENGGUNAKAN LAMBDA """
dataList = ['jjjjj', 'kkkkkk', 'aaaaaaa', 'yyyyyyyyy']
dataList.sort(key=lambda nama: len(nama))  # cara penggunaannya
print(f"sorted list by lambda \t\t= {dataList}")
print("\n")

""" FILTER """
dataAngka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def kurangDari(angka):
    return angka < 7


dataAngkaFilter = list(filter(kurangDari, dataAngka))
print(f"filter menggunakan fungsi \t= {dataAngkaFilter}")

dataAngkaFilter = list(filter(lambda angka: angka < 7, dataAngka))
print(f"filter menggunakan lambda \t= {dataAngkaFilter}")

# data genap
dataGenap = list(filter(lambda genap: (genap % 2 == 0), dataAngka))
print(f"filter angka genap lambda \t= {dataGenap}")

# data ganjil
dataGanjil = list(filter(lambda ganjil: (ganjil % 2), dataAngka))
print(f"filter angka ganjil lambda \t= {dataGanjil}")

# data kelipatan
dataKelipatan = list(filter(lambda kelipatan: (kelipatan % 3 == 0), dataAngka))
print(f"filter angka kelipatan 3 \t= {dataKelipatan}")
print("\n")

""" ANONYMOUS  FUNCTION """
hasil = (lambda x, y: x * y)(10, 8)
print(f"anounymous function \t= {hasil}")

# pangkat biasa menggunakan fungsi


def pangkat(angka, pangkat):
    return angka ** pangkat


print(f"fungsi biasa \t\t= {pangkat(5, 2)}")

# pangkat menggunakan lambda
def pangkatLambda(pangkat):
    return lambda angka : angka ** pangkat
pangkat2 = pangkatLambda(2)
print(f"pangkat 2 menggunakan lambda = {pangkat2(3)}")
pangkat5 = pangkatLambda(5)
print(f"pangkat 5 menggunakan lambda = {pangkat5(5)}")
print(f"pangkat bebas = {pangkatLambda(2)(5)}")