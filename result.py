import requests
import bs4
from PyPDF2 import PdfWriter

def info(url):
  saturs=requests.get(url)
  
  if saturs.status_code==200:
    lapa=bs4.BeautifulSoup(saturs.content, 'html.parser')
  
    nosaukums=lapa.find('h1', class_='header--title').text.strip()
    sastavdalas=[sastavdalas.text.strip() for sastavdalas in lapa.find_all('span', class_='ingredient__unit')]
    pagatavosana=[pagatavosana.text.strip() for pagatavosana in lapa.find_all('span', class_='step__text text')]
  
    recepte={
      'nosaukums':nosaukums,
      'sastavdalas':sastavdalas,
      'pagatavosana':pagatavosana,
    }

    return(recepte)
  
  else:
    print('Šodien pietiks ar ūdens un gaiss :)')

recepte_url=''
recepte=info(recepte_url)

print(recepte['nosaukums'])
print("Sastāvdaļas:")
for sastavdalas in recepte['sastavdalas']:
  print(sastavdalas)
print("Pagatavošana:")
for pagatavosana in recepte['pagatavosana']:
  print("-", pagatavosana)

pdfka=PdfWriter()

with open('recepte.pdf', 'wb') as f:
  pdfka.write(f)
