from random import randrange as rr
from fT_functions import *

repeatTime = 5
timeRecords = []

ready_check()
while repeatTime > 0:
    selected_word = the_last_sender()
    print (selected_word)
    t1 = time()
    ans = input('Type the word: ')
    t2 = time()
    timeDiff = round(t2-t1,5)
    if ans == selected_word:
        print(f'Your typing speed was {timeDiff} seconds.')
        timeRecords.append(timeDiff)
    else:
        print('wrong_text_here_kekw_lmao')
    sleep(0.1)
    repeatTime -= 1

# AVERAGE TIME ENJOYER
sum_of_times = 0
for i in timeRecords:
    sum_of_times += i
average_time = sum_of_times/len(timeRecords)

# HIGH SCORE
try:
    tt_data = open('topTyper.txt', 'r')
    top_typer = tt_data.read()
    top_typer = float(top_typer)
except: 
    open('topTyper.txt','w')
    top_typer = 10

improve = top_typer-(average_time)

if average_time < top_typer:
    top_typer = average_time
    f = open('topTyper.txt', 'w')
    f.write(str(top_typer))
    print(average_time)
    print(f'///// NEW RECORD! ///// Improved {round(improve,10)} seconds!')
else:
    print(average_time)
    print(f'You were {round(improve,5)} seconds late.')

# high score'u tek txt file'da ve tek komutla çalışır hale getir.
# f.readline() ile satır okusun, buraya sadece high_score(2) yazınca 3. satır gelsin vs.