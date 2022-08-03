import random, string

tamanho = int(input("Digite o tamanho da senha que você deseja: "))

chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,'`.;:/?]}[{^çÇ"

rnd = random.SystemRandom() # os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))