from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content
#objeto site recebendo o conteudo da requisicao http do site
soup = BeautifulSoup(site, 'html.parser')
# objeto soup está baixando o html do site
# print(soup.prettify())
#prettify transforma html em string e o print vai exibir o html

print(soup.title.string)
print(soup.a.string)
print(soup.p.string)