# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""


import redis
import os
import time
import pickle #Para serializar-deserializar el objeto
import pop_division as clase


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
print("setup:espera 3 segundos")
time.sleep(3)


while True:    
    tupla = r.lpop('queue_division')
    if tupla is None:
        print('se agotaron los elementos')        
        break
    
    tupla = pickle.loads(tupla)
    #print('monitor_pop.tupla: ', tupla)

    objeto = clase.Division(tupla)
    objeto.calcular()
    objeto.display()    

    time.sleep(2)