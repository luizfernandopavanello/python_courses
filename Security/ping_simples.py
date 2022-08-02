import os # importa o módulo ou biblioteca os (integra os programas e recursos do S.O.)

print('#' * 60)

ip_hosting = input('Digite o Ip ou host a ser verificado: ')

print('-' * 60)

os.system(f'ping -n 6 {ip_hosting}')
print('-' * 60)
