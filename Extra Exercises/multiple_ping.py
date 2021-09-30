import os #Importar o módulo ou biblbioteca os (integra os programas e recursos do sistema operacional do S.O

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping -n 2 {}'.format(ip))

