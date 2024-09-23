# operasi logika (boolean)

# operator pada operasi logika (boolean)
'''
    1. not
    2. or
    3. and
    4. xor
'''

# NOT
print("===NOT===")
x = False
y = not x
print("nilai x ", x)
print("---NOT---")
print("nilai y ", y)

# OR (jika salah satu true, maka hasilnya true)
print("===OR===")
x = True
y = True
z = x or y
print(x, "OR", y, "=", z)
x = True
y = False
z = x or y
print(x, "OR", y, "=", z)
x = False
y = False
z = x or y
print(x, "OR", y, "=", z)
x = False
y = True
z = x or y
print(x, "OR", y, "=", z)

# AND (jika dua buah nilainya true, maka hasilnya akan true )
print("===AND===")
x = True
y = True
z = x and y
print(x, "AND", y, "=", z)
x = True
y = False
z = x and y
print(x, "AND", y, "=", z)
x = False
y = False
z = x and y
print(x, "AND", y, "=", z)
x = False
y = True
z = x and y
print(x, "AND", y, "=", z)

# XOR (akan true jika salah satu nilai true)
print("===XOR===")
x = True
y = True
z = x ^ y
print(x, "XOR", y, "=", z)
x = True
y = False
z = x ^ y
print(x, "XOR", y, "=", z)
x = False
y = False
z = x ^ y
print(x, "XOR", y, "=", z)
x = False
y = True
z = x ^ y
print(x, "XOR", y, "=", z)