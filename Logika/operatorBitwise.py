# operasi bitwise adalah operasi biner atau binary

a = 9
b = 5

# bitwise OR (|)

c = a | b
print("======OR======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))

print("======(|)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))

# bitwise AND ($)

c = a & b
print("======AND======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))

print("======(&)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))

# bitwise XOR (^)

c = a ^ b
print("======XOR======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))

print("======(^)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))

# bitwise NOT (~)
c = ~a
print("======NOT======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
# print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))

print("======(~)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))

print("======(^)=====")
e = 0b0000001001
d = 0b1111111111
print("nilai: ", e^d, " , ", "binary: ", format(e^d, "08b"))

# shifting

# shift right (>>)
c = a >> 1
print("======(>>)======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
# print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))
print("======(>>)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))

# shift left (<<)
c = a >> 1
print("======(<<)======")
print("nilai a: ", a, " , ", "binary a: ", format(a, "08b"))
# print("nilai b: ", b, " , ", "binary b: ", format(b, "08b"))
print("======(<<)=====")
print("nilai c: ", c, " , ", "binary c: ", format(c, "08b"))