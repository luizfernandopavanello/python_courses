from threading import Thread
import time

def car(vel, pilot):
    trajeto = 0
    while trajeto <= 100:
        trajeto += vel
        time.sleep(0.5)
        print('Piloto: {} km: {} '.format(pilot, trajeto))


t_car1 = Thread(target=car, args=[1, 'Python'])
t_car2 = Thread(target=car, args=[1.5, 'Mamba'])

t_car1.start()
t_car2.start()
