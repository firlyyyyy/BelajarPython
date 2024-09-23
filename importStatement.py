""" IMPORT STATEMENT """

# 1. untuk menyambung program dari external
import contohImport1

# 2. import dengan data
import contohImport2

# data ada di namespace variable
print(contohImport2.data)

import requests
response = requests.get("https://www.python.org/")
print(response.status_code)