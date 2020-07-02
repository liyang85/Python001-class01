import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

ua_gc = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
ua_ipad = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

my_ua = ua_ipad
my_header = {'user-agent': my_ua}
my_url = 'https://m.maoyan.com/films?showType=3'

response = requests.get(my_url, headers=my_header)

soup = bs(response.text, 'html.parser')

for tags in soup.find_all('div', attrs={'class': 'classic-movies-list'}):
    for tag in tags.find_all('div', attrs={'class': 'movie-info'}, limit=10):

        name = tag.find('div', 'title').text
        category = tag.find('div', 'actors').text
        release_info = tag.find('div', 'show-info').text
        release_date = release_info[:10]

        film_info = [(name, category, release_date)]
        films = pd.DataFrame(data=film_info)
        films.to_csv('./maoyan_10_films.csv', mode='a', encoding='utf8', index=False, header=False)
