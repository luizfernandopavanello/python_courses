from threading import Thread
import time


def car(velocidade, piloto):
	trajeto = 0
	while trajeto <= 100:
		trajeto += velocidade
		time.sleep(0.5)
		print(f'Piloto: {piloto} Km: {trajeto} \n')


t_car1 = Thread(target=car, args=[1, 'Case'])
t_car2 = Thread(target=car, args=[2, 'Moly'])

t_car1.start()
t_car2.start()