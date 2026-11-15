import requests
import json

'''
#challenge1
print(requests.get("http://web-01.challs.olicyber.it/"))
#challenge2
print(requests.get("http://web-02.challs.olicyber.it/server-records", params = {'id': 'flag'}).text)
#challenge3
print(requests.get("http://web-03.challs.olicyber.it/flag", headers = {'X-Password': 'admin'}).text)

#challenge4
#by_default
curl http://web-04.challs.olicyber.it/users
print(requests.get("http://web-04.challs.olicyber.it/users", headers = {'Accept': 'application/xml'}).text)

#challenge5
print(requests.get("http://web-05.challs.olicyber.it/flag", cookies = {'password': 'admin'}).text)

#challenge6
s = requests.Session()
s.get('http://web-06.challs.olicyber.it/token')
# print(response.cookies.get('token'))
# print(response.cookies.get_dict())
print(s.get('http://web-06.challs.olicyber.it/flag').text)

#challenge7
response = requests.head("http://web-07.challs.olicyber.it/")
for key, value in response.headers.items():
	print(f'{key}: {value}')
# uso .items() perche se no itera solo key
# (response.headers e' gia' iterabile di per se ma ignora value)
# in requests gli oggetti non sono dizionari normali ma gli
# sviluppatori hanno implementato .items() per rispettare gli
# standard
	
#challenge8
# di base requests riconosce automanticamente il campo data come
# urlencoded

# per farlo manualmente:
# il formato urlencoded e' obsoleto ma legacy e ancora molto usato
# ma e' difficile da strutturare. 
# la librerira requests semplifica l'invio del formato tramite 
# l'uso di un dizionario

data = {'username': 'admin',
		'password': 'admin'}

headers = {'content-type': 'application/x-www-form-urlencoded'}


print(requests.post("http://web-08.challs.olicyber.it/login",
					headers = headers,
					data = data).text)

#challenge9
# XML e JSON sono molto piu moderni e facili da usare specialmente
# con JavaScript
# Automaticamente possiamo scrivere come argomento json=data
# e viene assegnato automaticamente l'header content-type json
# Manualmente:

data = {'username': 'admin',
		'password': 'admin'}

headers = {'content-type': 'application/json'}


print(requests.post("http://web-09.challs.olicyber.it/login",
					headers = headers,
					data = json.dumps(data)).text)







'''



# compatto
# print((requests.options('http://web-10.challs.olicyber.it/')).headers.get('Allow'))

response = requests.options('http://web-10.challs.olicyber.it/')
# per stampare tutti gli headers
# print(response.headers)

# per stampare header 'Allow' uso il metodo get per la chiave
print('Allowed methods: ' + response.headers.get('Allow') + '\n')


methods = ['put', 'patch', 'post']
for method in methods:
	print(f'METHOD: {method}')
	response = requests.request(method, 'http://web-10.challs.olicyber.it/')
	for key, val in response.headers.items():
		print(f'\t-> {key}: {val}')




