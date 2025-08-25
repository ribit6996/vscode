import random 
import _thread
import time
import os

random1 = random.randrange(1, 1000000)
attempts = 0
time1 = time.asctime()

while True:
    random2 = random.randrange(1, 1000000)
    
    attempts += 1
    
    print(random2)
    
    if random1 == random2:
        print("popitok:", attempts, "chislo:", random1,)
        print("vremya nachala:", time1, "vremya konca:", time.asctime())
        break





























