# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""


import redis
import os
import time
import pickle #Para serializar-deserializar el objeto
from push_metodos import get_entero


#Iniciamos la conexión con Redis
r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)
redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)
        
print("setup:redis alive")


#Eliminamos los elementos residuales de la lista
while True:    
    i = r.lpop('queue_division')
    if i is None:
        print('setup:limpieza de queue')
        break


#Valores predeterminados para las tuplas
cociente, residuo, operacion = 0, 0, ''

i = 0
while i <= 100:
    dividendo = get_entero(100, 1000)
    divisor = get_entero(1, 100)
    
    tupla = (dividendo, divisor, cociente, residuo, operacion)
    r.rpush('queue_division', pickle.dumps(tupla))
    #print('monitor_push.tupla: ', tupla)

    i+=1
    time.sleep(1)