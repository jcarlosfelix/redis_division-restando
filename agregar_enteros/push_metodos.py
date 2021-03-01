import random


def get_entero(rango_min, rango_max):
	return (random.randint(rango_min, rango_max) * calcular_signo())

def calcular_signo():
    return {True: 1, False: -1} [random.randint(0, 1) == 1]
