import requests
import bs4
from PyPDF2 import PdWriter

url=""
saturs=requests.get(url)

if saturs.status_code==200:
  lapa=bs4.BeautifulSoup(saturs.content, 'html.parser')

  nosaukums=lapa.find('h1', class_='svelte-1muv3s8').text.strip()
  sastavdalas=[sastavdalas.text.strip() for sastavdalas in lapa.find_all('span', class_='ingredient-text svelte-1dqq0pw')]
  daudzums=[daudzums.text.strip() for daudzums in lapa.find_all('span', class_='ingredient-quantity svelte-1dqq0pw')]
  pagatavosana=[pagatavosana.text.strip() for pagatavosana in lapa.find_all('li', class_='direction svelte-1dqq0pw')]

  recepte={
    'nosaukums':nosaukums,
    'daudzums':daudzums,
    'sastavdalas':sastavdalas,
    'pagatavosana':pagatavosana,
  }

else:
  print('Šodien pietiks ar ūdens un gaiss :)')
