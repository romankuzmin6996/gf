from bs4 import BeautifulSoup
import requests

def atrodi_virsrakstu(url):
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, "html.parser")
  virsraksti = []
  for h1 in soup.find_all("h1"):
    virsraksti = h1.text
    virsraksti.append(virsraksti)
  return virsraksti
  
url = input("Ievadi URL:")
virsraksti = atrodi_virsrakstu(url)
print(virsraksti)