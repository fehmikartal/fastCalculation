from time import time,sleep
from random import randint as ri

def ready_check():
    i = 3
    while i >0:
        print(i)
        sleep(1)
        i -= 1

def the_last_sender():
    with open('words.txt','r') as f:
        word_list = f.readlines()
        randnum = ri(0,9999)
    return word_list[randnum][:-1]

def time_check(td):
    if td <= 5:
        return True