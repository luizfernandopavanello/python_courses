import os #Importar o módulo ou biblbioteca os (integra os programas e recursos do sistema operacional do S.O

# Criando uma variável que vai receber do usuario um ip
ip_host = input('Digite o Ip ou host a ser verificado: ')

# Chamando system da biblioteca OS - comando ping -n → número de pacotes que serao 6
os.system('ping -n 6 {}'.format(ip_host))
