import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP Externo')
print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg.: {org}')