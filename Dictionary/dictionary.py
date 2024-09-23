# list --> array, mengakses data menggunakan index
dataList = ['a', 'b', 'c']
# print(dataList[1])
# print("\n")

# dictionary (dict) --> associative array
# dictionary di akses melalui identifier-nya --> key
dict = {
    # 'key': 'value',
    'ap': 'asep',
    'ud': 'udin',
    'jb': 'jibar',
    'number': 12,
    'list': dataList,    
}  # dictionary menggunakan kurung kurawal
print(f"key ap : {dict['ap']}")  # mengakses value dengan key 'ap'
print(f"key number : {dict['number']}")
print(f"key list  : {dict['list']}")  # mengakses value dengan key 'list'