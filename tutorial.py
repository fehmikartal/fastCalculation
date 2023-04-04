from random import randint
import time

i = 15

while i > 0:
    hard = False
    n1 = randint(11,19)
    n2= randint(3,9)
    t1 = time.time()
    answer = input(f"{str(n1)[-1]}-{n2}=")
    t2 = time.time()
    timeDiff = t2-t1
    if timeDiff > 2.5: hard=True
    if int(answer) == n1-n2:
        print(round(timeDiff,4))
    else:
        print(f'YANLIŞ. CEVAP : {timeDiff}')
        hard=True
    if hard:
        with open("hard.txt","a+") as f:
            f.write(f"{n1}-{n2}={n1-n2}\n")
    i -= 1