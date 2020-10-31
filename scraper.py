import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/all-new-echo-dot-4th-generation-smart-speaker-with-alexa-charcoal/dp/B084DWCZXZ/ref=sr_1_1?dchild=1&keywords=ALEXA&qid=1604161448&sr=8-1'

headers = {"User-Agent" :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
