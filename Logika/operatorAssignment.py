# operasi yang dilakukan dengan penyingkatan

a = 5  # ini adalah assignment
print("nilai a: ", a)

a += 1  # ini artinya adalah a = a + 1
print("nilai a += 1, nilai a: ", a)

a -= 2  # ini artinya a = a - 2
print("nilai a -= 2, niali a: ", a)

a *= 2  # ini artinya a = a * 2
print("nilai a *= 2, nilai a: ", a)

a /= 2  # ini artinya a = a / 2
print("nilai a /= 2, nilai a: ", a)

b = 10
print("\nnilai b: ", b)

b %= 3  # modulus (sisa bagi)
print("nilai b %= 3, nilai b: ", b)

b = 10
print("\nnilai b: ", b)

b //= 2  # floor division
print("nilai b //= 2, nilai b: ", b)

a = 5
print("nilai a: ", a)

a **= 3  # pangkat atau eksponen
print("nilai a **= 3, nilai a: ", a)

# operasi bitwise

# OR (|)
c = True
print("\nnilai c: ", c)

c |= False
print("nilai c |= False, nilai c: ", c)

# AND (&)
c = False
print("\nnilai c: ", c)

c &= True
print("nilai c &= True, nilai c: ", c)

# XOR (^)
c = True
print("\nnilai c: ", c)

c ^= True
print("nilai c ^= True, nilai c: ", c)

# shifting right
d = 0b0100
print("\nnilai d: ", format(d, "04b"))

d >>= 2
print("nilai d >>= 2, nilai d: ", format(d, "04b"))

# shifting left
d = 0b0001
print("nilai d: ", format(d, "04b"))

d <<= 2
print("nilai d <<= 2, nilai d: ", format(d, "04b"))