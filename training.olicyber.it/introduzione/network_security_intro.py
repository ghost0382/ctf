import requests
import json
from bs4 import BeautifulSoup, Comment

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


#challenge10
# compatto
# print((requests.options('http://web-10.challs.olicyber.it/')).headers.get('Allow'))

# response = requests.options('http://web-10.challs.olicyber.it/')
# per stampare tutti gli headers
# print(response.headers)

# per stampare header 'Allow' uso il metodo get per la chiave
# print('Allowed methods: ' + response.headers.get('Allow') + '\n')

'''
'''
methods = ['get', 'put', 'patch']
for method in methods:
	print(f'METHOD: {method}')
	response = requests.request(method, 'http://web-10.challs.olicyber.it/')
	for key, val in response.headers.items():
		print(f'\t-> {key}: {val}')
print('')
'''
'''
print(requests.put('http://web-10.challs.olicyber.it/').headers.get('X-Flag'))


#challenge11
flag = ""
csrf_token = None
s = requests.Session()
response = s.post('http://web-11.challs.olicyber.it/login', json={'username':'admin', 'password':'admin'})
# da controllare uso di [] e di () con items() (???)
if response.status_code == 200:
	csrf_token = response.json()['csrf']
else:
	print("Impossibile accedere al sito")
	exit(1)
	
for index in range(4):
	response = s.get('http://web-11.challs.olicyber.it/flag_piece', params={'index': index, 'csrf': csrf_token})
	if response.status_code == 200:
		csrf_token = response.json()['csrf']
		flag += response.json()['flag_piece']	
	else:
		print("Impossibile accedere alla risorsa")
		exit(1)
print(flag)


#challenge12
# creo un oggetto Soup dove prendo il corpo della response e 
# utilizzo un parser (html.parser) per interpretare la stringa
soup = BeautifulSoup(requests.get('http://web-12.challs.olicyber.it/').text, 'html.parser')

# cerco in soup tutti i paragrafi.
# p e' una lista di oggetti BeautifulSoup

#	p = [
#   	 <p>Challenge 1</p>,
#   	 <p>Challenge 2</p>
#	]

# per accedere p[<numero_oggetto>]

p = soup.find_all('p')
for _ in p:
	# per accedere al contenuto dell'oggetto beautifulsoup.tag
	# uso .text (diverso da .text di requests)
	if 'flag' in _.text:
		print(_.text)


#challenge13
flag = 'flag{'
soup = BeautifulSoup(requests.get('http://web-13.challs.olicyber.it/').text, 'html.parser')
p = soup.find_all('span')
for _ in p:
	flag += _.text 
flag += '}'
print(flag)


#challenge14
soup = BeautifulSoup(requests.get('http://web-14.challs.olicyber.it/').text, 'html.parser')

# def is_comment(text):
#	return isinstance(text, Comment)

# non serve specificare l'argomento perche viene passato automaticamente dal
# oggetto chiamante (in questo caso soup)
# comments = soup.find_all(string = is_comment)

# lambda expression
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for comment in comments:
	if 'flag' in comment:
		print(comment)

'''






