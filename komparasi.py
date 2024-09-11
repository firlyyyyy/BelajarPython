# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# operator pada operasi komperasi
'''
    1. > : lebih besar
    2. < : kurang dari
    3. >= : lebih besar sama dengan
    4. <= : kurang dari sama dengan
    5. == : sama dengan
    6. != : tidak sama dengan
    7. is
    8. is not
'''

a = 10
b = 5

# lebih besar >
print("===LEBIH BESAR===")
hasil = a > 11
print(a, ">", 11, ":", hasil)

# kurang dari
print("===KURANG DARI===")
hasil = a < 11
print(a, "<", 11, ":", hasil)

# lebih besar sama dengan
print("===LEBIH BESAR SAMA DENGAN===")
hasil = a >= 10
print(a, ">=", 10, ":", hasil)

# kurang dari sama dengan
print("===KURANG DARI SAMA DENGAN===")
hasil = a <= 10
print(a, "<=", 10, ":", hasil)

# sama dengan
print("===SAMA DENGAN===")
hasil = a == 10
print(a, "==", 10, ":", hasil)

# tidak sama dengan
print("===TIDAK SAMA DENGAN===")
hasil = a != 10
print(a, "!=", 10, ":", hasil)

# is sebagai komparasi object identity
print("===OBJECT IDENTITY(is)===")
x = 10  # ini adalah assignment membuat object
y = 10
print("niali x : ", x, hex(id(x)))
print("nilai y : ", y, hex(id(y)))
hasil = x is y
print("hasil dari nilai x", x, "dan y", y, "adalah ", hasil)

# is sebagai komparasi object identity
print("===OBJECT IDENTITY(is not)===")
x = 10  # ini adalah assignment membuat object
y = 10
print("niali x : ", x, hex(id(x)))
print("nilai y : ", y, hex(id(y)))
hasil = x is not y
print("hasil dari nilai x", x, "dan y", y, "adalah ", hasil)