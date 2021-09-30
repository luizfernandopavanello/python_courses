import ipaddress

ip = '192.168.0.1'

rede = ipaddress.ip_network(ip)

print(rede)