import requests
import bs4

url=""
saturs=requests.get(url)

if saturs.status_code==200:
  lapa=bs4.BeautifulSoup(saturs.content, 'html.parser')

  nosaukums=lapa.find('h1', class_='svelte-1muv3s8').text.strip()
  

else:
  print('Šodien pietiks ar ūdens un gaiss :)')
