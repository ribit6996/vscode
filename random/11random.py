import random 

attempts = 0

while True:
    print(random.randint(1, 100))
    attempts += 1

    if attempts == 100000:
        break
    if attempts % 1000 == 0:
        print(f"attempts: {attempts}")
