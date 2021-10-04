from tqdm import tqdm
import time

# forma mais simples
# for i in tqdm(range(10)):
#     time.sleep(1)

# lista = [1, 2, 3, 10, 15]
#
# for item in tqdm(lista):
#     time.sleep(1)
#
# with tqdm(total=100) as barra_progresso:
#     for i in range(10):
#         time.sleep(1)
#         barra_progresso.update(1)

# quero entregar pra cidade do Rio de Janeiro
import requests


# passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")
# passo 2: pegar as informações de cada cep
enderecos_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    # passo 3: verificar se a cidade é RIo de Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    # passo 4: printar o cep e o bairro
    if cidade == "Rio de Janeiro":
        enderecos_entrega.append((cep, bairro))
print(enderecos_entrega)