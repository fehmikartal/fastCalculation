from random import randrange as rr
from time import time, sleep
sleep(rr(1,4))
print ('Press ENTER!')
t1 = time()
ans = input('')
t2 = time()

# HIGH SCORE
try:
    tr_data = open('topReact.txt', 'r')
    top_react = tr_data.read()
    top_react = float(top_react)
except: 
    open('topReact.txt','w')
    top_react = 10

improve = top_react-(t2-t1)

if t2-t1 == 0.0:
    print('You pressed early.')
else:
    print('Your reaction time was ' + str(round(t2-t1,5)) + ' seconds.')

    if t2-t1 < top_react:
        top_react = t2-t1
        f = open('topReact.txt', 'w')
        f.write(str(top_react))
        print(f'///// NEW RECORD! ///// Improved {round(improve,10)} seconds!')
    else:
        print(f'You were {round(improve,5)} seconds late.')

# bilinen hatalar
# - press enter yazısı çıkmadan basarsan 0.03 gibi saniyelere ulaşıyorsun. 
# yazı çıkmadan önce basmak elenmeye sebep olmalı.