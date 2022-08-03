import hashlib

arq1 = 'arquivo1.txt'
arq2 = 'arquivo2.txt'


hash1 = hashlib.new('sha256')
hash1.update(open(arq1, 'rb').read())


hash2 = hashlib.new('sha256')
hash2.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
	print(f'O arquivo: {arq1} é diferente do arquivo: {arq2}.')
	print('O hash do arquivo 1 é: ', hash1.hexdigest())
	print('O hash do arquivo 2 é: ', hash2.hexdigest())
else:
	print(f'O arquivo: {arq1} é igual ao arquivo: {arq2}.')
	print('O hash do arquivo 1 é: ', hash1.hexdigest())
	print('O hash do arquivo 2 é: ', hash2.hexdigest())