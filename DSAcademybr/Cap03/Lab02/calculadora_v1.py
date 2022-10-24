# Calculadora em Python

print("\n******************* Python Calculator *******************")

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y


print('\nSelecione o número da operação desejada: \n')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

while True:
	escolha = input('\nDigite sua opção (1/2/3/4): ')

	#checar se a escolha é uma das opções
	if escolha in ('1', '2', '3', '4'):
		num1 = int(input('\nDigite o primeiro número: '))
		num2 = int(input('\nDigite o segundo número: '))

		if escolha == '1':
			print(num1, '+', num2, '=', add(num1, num2))

		elif escolha == '2':
			print(num1, '-', num2, '=', subtract(num1, num2))

		elif escolha == '3':
			print(num1, '*', num2, '=', multiply(num1, num2))

		elif escolha == '4':
			print(num1, '/', num2, '=', divide(num1, num2))

		mais_calculo = input('Vamos continuar calculando? (s/n): ')
		if mais_calculo == 'n':
			break
			
	else:
		print('\nOpção errada...')
