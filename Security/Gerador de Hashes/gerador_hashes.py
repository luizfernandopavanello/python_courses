import hashlib

string = input('Digite o texto a ser hasheado: ')

menu = int(input(''' ### MENU - Escolha o tipo de Hash: ###
				1) MD5
				2) SHA1
				3) SHA256
				4) SHA512
				Digite o número do hash a ser gerado: '''))

if menu == 1:
	result = hashlib.md5(string.encode('utf-8'))
	print(f'O hash MD5 da string {string} é:', result.hexdigest())
elif menu == 2:
	result = hashlib.sha1(string.encode('utf-8'))
	print(f'O hash SHA1 da string {string} é:', result.hexdigest())
elif menu == 3:
	result = hashlib.sha256(string.encode('utf-8'))
	print(f'O hash SHA256 da string {string} é:', result.hexdigest())
elif menu == 4:
	result = hashlib.sha512(string.encode('utf-8'))
	print(f'O hash SHA512 da string {string} é:', result.hexdigest())
else:
	print('Algo de errado está certo...')
