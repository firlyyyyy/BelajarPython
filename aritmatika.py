# operasi aritmatika

a = 10
b = 3

# tambah
print("===PERTAMBAHAN===")
hasil = a + b
print(a, "+", b, "= ", hasil)

# kurang 
print("===PENGURANGAN===")
hasil = a - b
print(a, "-", b, "= ", hasil)

# kali
print("===PERKALIAN===")
hasil = a * b
print(a, "x", b, "= ", hasil)

# bagi
print("===PEMBAGIAN===")
hasil = a / b
print(a, "/", b, "= ", hasil)


# eksponen(pangkat) dilambangkan dengan **
print("===EKSPONEN===")
hasil = a ** b
print(hasil)

# modulus(sisa bagi) dilambagkan dengan %
print("===MODULUS===")
hasil = a % b
print(hasil)

# floor division dilambangkan dengan //
print("===FLOOR DIVISION===")
hasil = a // b
print(hasil)

# prioritas operasi, operation precedence

'''
urutan prioritas operasi:
    1. ()
    2. eksponen **
    3. perkalian, modulus, pembagian
    4. pertambahan, pengurangan
'''

a = 3
b = 4
c = 5
hasil = a // b ** a / b + a - c * a / b + c
print(hasil)