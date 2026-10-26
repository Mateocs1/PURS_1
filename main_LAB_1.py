import requests

"""
# 2. Zadatak 


response = requests.get(f'http://192.168.83.5/login')

for k, v in response.headers.items():
    print(f'{k}: {v}')
"""

 # 3. Zadatak 
""" 
payload = {
    "username": 'PURS',
    "password" : '1234'
}
response = requests.post('http://192.168.83.5/login', json=payload)

for k, v in response.headers.items():
    print(f'{k}: {v}')
print()
print(response.text)
print(response.status_code)
print(response.json)
"""

# 4. Zadatak
"""
response = requests.get(f'http://192.168.83.5/temperatura')


for k, v in response.headers.items():
    print(f'{k}: {v}')

print()
print(response.text)
print(response.status_code)
print(response.json)    

podatci = response.json()
temp = podatci["temperatura"]
print("Temperatura je:", temp)
"""

# 5. Zadatak
"""
payload = {
    "temperatura" : '24'
}

response = requests.post('http://192.168.83.5/temperatura', json=payload)

for k, v in response.headers.items():
    print(f'{k}: {v}')

print()
print(response.text)
print(response.status_code)


"""
# 6. Zadatak
"""
parametar = {
    "id" : '1'
}

response = requests.delete('http://192.168.83.5/temperatura', params=parametar)

for k, v in response.headers.items():
    print(f'{k}: {v}')

print()
print(response.text)
print(response.status_code)
"""

# 7. Zadatak

response = requests.get(f'http://api.ipify.org/?format=json')


for k, v in response.headers.items():
    print(f'{k}: {v}')

print()
print(response.text)
print(response.status_code)
print(response.json)    

podatci = response.json()
temp = podatci["ip"]
print("IP je:", temp)