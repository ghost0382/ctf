import requests
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin


# challenge16
# target: 

# restituisce il titolo della pagina
def h1_scrape(webpage):

	return webpage.find('h1')

# restituisce una lista di path snippati per continuare la ricerca
def href_scrape(webpage):
	paths = []
	a_list = webpage.find_all('a')

	for a in a_list:
		href = a.get('href')
		if href:
			paths.append(href)

	return paths
		
		
to_visit = ['http://web-16.challs.olicyber.it/']
discovered = {'http://web-16.challs.olicyber.it/'}
visited = set()
flag = ''

while to_visit:
	current_url = to_visit.pop()

	if current_url in visited:
		continue

	visited.add(current_url)
	
	response = requests.get(current_url)
	# timeout=5
	webpage = BeautifulSoup(response.text, 'html.parser')

	h1 = h1_scrape(webpage)
	
	
	# debug =======================================================
	print(
		f"Requests n: {len(visited)} @ {current_url}. Total sites discovered: {len(discovered)}.", end = '\r')
	# =============================================================


	if h1 and 'flag' in h1.text.lower():
		flag = h1.text.strip()
		break

	# estrazione nuovi url
	for path in href_scrape(webpage):
		absolute_url = urljoin(current_url, path)
		if absolute_url not in discovered:
			discovered.add(absolute_url)
			to_visit.append(absolute_url)

if flag:
	print('\n' + flag)
else:
	print('Flag not found')
