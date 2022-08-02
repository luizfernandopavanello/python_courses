import os
import time


with open('hosts.txt') as file:
	dump = file.read()
	dump = dump.splitlines()

	for ip in dump:
		print('Verificando o ip: ', ip)
		print('-' * 60)
		os.system(f'ping -n 2 {ip}')
		time.sleep(3)
		print('-' * 60)

print('End...')
