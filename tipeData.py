# tipe data integer
data_integer = 1
print(data_integer, type(data_integer))

# tipe data float
data_float = 1.5
print(data_float, type(data_float))

# tipe data string
data_string = "hello world"
print(data_string, type(data_string))

# tipe data boolean (true false)
data_boolean = True
print(data_boolean, type(data_boolean))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print(data_complex, type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print(data_c_double, type(data_c_double))
