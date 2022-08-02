import socket

s.socket.soket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = "Servidor: Olá Cliente, tudo certo?"

while 1:
	dados, end = s.recvfrom(4096)

	if dados:
		print('Servidor enviando mensagem...')
		s.sento(dados + (mensagem.encode()), end)
