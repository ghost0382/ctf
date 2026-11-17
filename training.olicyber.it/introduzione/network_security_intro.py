import requests
import json
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin
import re

def find_flag(text):
	start = text.find('flag{')
	end = text.find('}', start)
	return text[start:(end+1)]

# challenge1
# target: flag is in the body of the url
print(requests.get("http://web-01.challs.olicyber.it/").text)

# challenge2
# target: flag is accessible via url param id
print(requests.get("http://web-02.challs.olicyber.it/server-records", params = {'id': 'flag'}).text)

# challenge3
# target: flag is accessible via custom header X-Password
print(requests.get("http://web-03.challs.olicyber.it/flag", headers = {'X-Password': 'admin'}).text)

# challenge4
# target: flag is accessible via custom Accept header
# by_default curl already accepts 'application/xml' 
# curl http://web-04.challs.olicyber.it/users
response = requests.get("http://web-04.challs.olicyber.it/users", headers = {'Accept': 'application/xml'}).text
print(find_flag(response))

# challenge5
# target: flag is accessible via custom Cookies header
print(requests.get("http://web-05.challs.olicyber.it/flag", cookies = {'password': 'admin'}).text)

# challenge6
# target: using Session obj, we download a session cookie connecting to /token
# then we access /flag 
s = requests.Session()
s.get('http://web-06.challs.olicyber.it/token')
print(s.get('http://web-06.challs.olicyber.it/flag').text)

''' NOTES:
# per visualizzare tutti i cookie installati:
	>	print(response.cookies.get_dict())
# per visualizzare un cookie specifico:
	>	print(response.cookies.get('token'))
'''

# challenge7
# target: flag is stored in one of the response header 
response = requests.head("http://web-07.challs.olicyber.it/")
for key, value in response.headers.items():
	if 'flag' in value:
		print(value)

''' NOTE:
in requests gli oggetti non sono dizionari normali ma gli
sviluppatori hanno implementato .items() per rispettare gli
standard

response.headers quindi e' gia' iterabile di per se ma non fa l'unpaking
uso .items() per fare l'unpaking e accedere al campo key e value
In alternativa:
.items()	> accedo a .key e .value
.keys()		> accedo a .key
.values()	> accedo a .value
'''

# challenge8
# target: flag is accessible via post request and urlencoded login data

data = {'username': 'admin',
		'password': 'admin'}

headers = {'content-type': 'application/x-www-form-urlencoded'}


print(requests.post("http://web-08.challs.olicyber.it/login",
					headers = headers,
					data = data).text)

''' NOTE
di base requests riconosce automanticamente il campo data come
urlencoded, quindi non ci sarebbe bisogno di specificarlo nell'url

per farlo manualmente:
il formato urlencoded e' obsoleto poiche piuttosto difficile da
strutturare ma legacy quindi ancora molto usato

la librerira requests semplifica l'invio del formato tramite l'uso di un
dizionario
'''

# challenge9
# target: flag is accessible via post request and json login data

data = {'username': 'admin',
		'password': 'admin'}

headers = {'content-type': 'application/json'}


response = requests.post("http://web-09.challs.olicyber.it/login",
					headers = headers,
					data = json.dumps(data)).text

print(find_flag(response))

''' NOTE:
XML e JSON sono molto piu moderni e facili da usare specialmente
con JavaScript.
Automaticamente possiamo scrivere come argomento json=data
e viene assegnato automaticamente l'header content-type json. 
Manualmente la soluzione e' mostrata sopra.
'''

# challenge10
# target: flag is accessible via not allowed request method


''' NOTE: 
Con option ottengo i metodi disponibili:
# print(requests.options('http://web-10.challs.olicyber.it/'))

Per stampare tutti gli headers:
# print(response.headers)

Per stampare solo l'header 'Allow' uso il metodo get:
# print('Allowed methods: ' + response.headers.get('Allow') + '\n')


Di seguito una soluzione piu estesa:
# allowed methods:
print((requests.options('http://web-10.challs.olicyber.it/')).headers.get('Allow'))

methods = ['get', 'put', 'patch']
for method in methods:
	print(f'METHOD: {method}')
	response = requests.request(method, 'http://web-10.challs.olicyber.it/')
	for key, val in response.headers.items():
		print(f'\t-> {key}: {val}')
print('')
'''
print(requests.put('http://web-10.challs.olicyber.it/').headers.get('X-Flag'))


# challenge11
# target: flag is optainable by loggin at /login to get session cookie
# and csrf token and requesting each piece of flag using index + new
# csrf token
 
flag = ''
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



soup = BeautifulSoup(requests.get('http://web-15.challs.olicyber.it/').text, 'html.parser')
links = soup.find_all('link')
scripts = soup.find_all('script')

paths = []
for link in links:
	paths.append(link.get('href'))
for script in scripts:
	paths.append(script.get('src'))

for path in paths:
	response = requests.get(urljoin('http://web-15.challs.olicyber.it/', path)).text
	start = response.find('flag{')
	end = response.find('}', start)
	
	if (start != -1) and (end != -1): 
		print(response[start:(end + 1)])
