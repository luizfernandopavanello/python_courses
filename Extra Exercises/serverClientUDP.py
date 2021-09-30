import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com sucesso')

host = 'localhost'
porta = 5433
message = 'Olá servidor.'

try:
    print('Cliente: ' + message)
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechando a conexao.')
    s.close()