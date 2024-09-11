# list

# kumpulan data numbers
data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ["a", "b", "c"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, "a", True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 9, 2)  # range(start, stop, step)
data_list = list(data_range)  # agar data range menjadi list
print(data_list)

# membuat list dengan for loop, list comprehension
data_list_for = [i for i in range(0, 9)]
print(data_list_for)

# membuat list pakai for pakai if
data_list_for_if = [i for i in range(0, 10) if i != 5]
print(data_list_for_if)

data_list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(data_list_for_if)

data_list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(data_list_for_if)