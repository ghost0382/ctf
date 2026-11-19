import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import perf_counter


class WebCrawler:

    def __init__(self, start_url):
        self.start_url = start_url

        self.to_visit = [start_url]
        self.discovered = {start_url}
        self.visited = set()

        self.flag = None
        self.last_urls = []

        self.total_requests = 0
        self.total_links = 0
        self.duplicates = 0
        self.errors = 0

        self.total_response_time = 0
        self.start_time = None
        self.end_time = None

    def h1_scrape(self, webpage):
        return webpage.find('h1')

    def href_scrape(self, webpage):
        return [
            a.get('href')
            for a in webpage.find_all('a')
            if a.get('href')
        ]

    def crawl(self):

        self.start_time = perf_counter()

        while self.to_visit:

            current_url = self.to_visit.pop()

            if current_url in self.visited:
                continue

            self.visited.add(current_url)

            try:
                start = perf_counter()

                response = requests.get(
                    current_url,
                    timeout=5
                )

                elapsed = perf_counter() - start

                self.total_response_time += elapsed
                self.total_requests += 1

                response.raise_for_status()

                webpage = BeautifulSoup(
                    response.text,
                    'html.parser'
                )

                self.last_urls.append(current_url)
                self.last_urls = self.last_urls[-10:]

                # Controllo flag
                h1 = self.h1_scrape(webpage)

                if h1 and 'flag' in h1.text.lower():
                    self.flag = h1.text.strip()
                    break

                # Estrazione link
                for path in self.href_scrape(webpage):

                    absolute_url = urljoin(
                        current_url,
                        path
                    )

                    # Limitiamo il crawler al dominio iniziale
                    if absolute_url.startswith(self.start_url.split('/')[0] + '//' + self.start_url.split('/')[2]):

                        self.total_links += 1

                        if absolute_url in self.discovered:
                            self.duplicates += 1
                            continue

                        self.discovered.add(absolute_url)
                        self.to_visit.append(absolute_url)

            except requests.RequestException:
                self.errors += 1

        self.end_time = perf_counter()

    @property
    def elapsed(self):
        if self.start_time is None:
            return 0

        end = self.end_time or perf_counter()
        return end - self.start_time

    @property
    def average_response_time(self):
        if not self.total_requests:
            return 0

        return self.total_response_time / self.total_requests

    @property
    def pages_per_second(self):
        if not self.elapsed:
            return 0

        return self.total_requests / self.elapsed
