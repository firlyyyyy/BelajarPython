# teknik menduplikat list

a = ["ab", "aa", "ac"]
print(f"a = {a}\n")

b = a  # pass by reference
print(f"b = {b}\n")

# merubah nilai a
a[0] = "ad"
print(f"a = {a}\n")
b.sort()
print(f"a = {a}")
print(f"b = {b}\n")

# address a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}\n")

# menduplikat list
c = a.copy()  # copy() --> digunakan untuk menduplikat data yang ada di a dengan memori yang berbeda
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}\n")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}\n")

c[0] = "ad"
print(f"a = {a}")
print(f"c = {c}\n")