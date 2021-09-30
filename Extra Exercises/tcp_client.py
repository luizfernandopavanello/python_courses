import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexao falhou')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso.')

    HostAlvo = input('Digite o host a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Clienet TCP conectado no Host ' + HostAlvo + 'e na porta ' + PortaAlvo)
        s.shutdown(2)
    except socket.error(e):
        print('Conexao falhou Host ' + HostAlvo + 'e na porta ' + PortaAlvo)
        print('Error: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()