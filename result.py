import requests
import bs4

def info(url):
  saturs=requests.get(url)
  
  if saturs.status_code==200:
    lapa=bs4.BeautifulSoup(saturs.content, 'html.parser')
  
    nosaukums=lapa.find('h1', class_='heading--sizing').text.strip()
    sastavdalas=[sastavdalas.text.strip() for sastavdalas in lapa.find_all('li', class_='recipe-ingredients__item')]
    pagatavosana=[pagatavosana.text.strip() for pagatavosana in lapa.find_all('div', class_='recipe-step__body')]
  
    recepte={
      'nosaukums':nosaukums,
      'sastavdalas':sastavdalas,
      'pagatavosana':pagatavosana,
    }

    return(recepte)
  
  else:
    print('Radījās kļūda. Pārbaudiet URL.')

recepte_url='IEVIETOT_URL'
recepte=info(recepte_url)

print(recepte['nosaukums'])
print("Sastāvdaļas:")
for sastavdalas in recepte['sastavdalas']:
  print("-", sastavdalas)
print("Pagatavošana:")
for pagatavosana in recepte['pagatavosana']:
  print(pagatavosana)
