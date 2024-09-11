# casting tipe data adalah merubah satu tipe data ke tipe data yang lain

print("=====INTEGER=====")

# tipe data int
data_int = 10
print(data_int, "tipe ", type(data_int))

data_float = float(data_int)
print(data_float, "tipe ", type(data_float))

data_str = str(data_int)
print(data_str, "tipe ", type(data_str))

data_bool = bool(data_int)
print(data_bool, "tipe ", type(data_bool))

from ctypes import c_double, c_char

data_c_double = c_double(data_int)
print(data_c_double, "tipe ", type(data_c_double))

print("=====FLOAT=====")

# tipe data float
data_float = 1.5
print(data_float, "tipe ", type(data_float))

data_int = int(data_float)
print(data_int, "tipe ", type(data_int))

data_str = str(data_float)
print(data_str, "tipe ", type(data_str))

data_bool = bool(data_float)
print(data_bool, "tipe ", type(data_bool))

print("=====BOOLEAN=====")

# tipe data boolean
data_bool = True
print(data_bool, "tipe ", type(data_bool))

data_int = int(data_bool)
print(data_int, "tipe ", type(data_int))

data_float = float(data_bool)
print(data_float, "tipe ", type(data_float))

data_str = str(data_bool)
print(data_str, "tipe ", type(data_str))

print("=====STRING=====")

# tipe data string
data_str = ""
print(data_str, "tipe ", type(data_str))

data_int = int(data_str)
print(data_int, "tipe ", type(data_int))

data_float = float(data_str)
print(data_float, "tipe ", type(data_float))

data_bool = bool(data_str)
print(data_bool, "tipe ", data_bool)