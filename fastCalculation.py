import time
from random import randint as ri

# SETTINGS
repeatTime = 2                                                      # soru sayısı
limit = 2                                                           # gelen sayıların basamak sayısı (maksimum)
# username = 'GloRudd'                                              # for a future project

# VARIABLES
points = 0
max_points = repeatTime*50 + repeatTime*(limit-1)*5 + 5
line = '-------------------------'
new_record = False
timeRecords = []
maxNum = (limit-1)*100
operations = ['+','-']

# FUNCTIONS
def add_points(td):
    if td <= 5:
        return True

while repeatTime > 0:
    operationRandomizer = ri(0,len(operations)-1)
    operation = operations[operationRandomizer]
    n1 = ri(0,maxNum)
    n2 = ri(0,maxNum)
    print(f"{n1} {operation} {n2}")
    t1 = time.time()
    ans = int(input('= '))
    t2 = time.time()
    timeDiff = t2-t1
    if operation == '+':
        if ans == n1+n2:
            print(str(round(timeDiff, 4)) + ' saniye')
            timeRecords.append(timeDiff)
            if add_points(timeDiff): points += round((5-timeDiff)*10)
        else:
            print(f'Yanlış Cevap. (Doğru: {n1+n2}, Cevabın: {ans})')
    elif operation == '-':
        if ans == n1-n2:
            print(str(round(timeDiff, 4)) + ' saniye')
            timeRecords.append(timeDiff)
            if add_points(timeDiff): points += round((5-timeDiff)*10)
        else:
            print(f'Yanlış Cevap. (Doğru: {n1-n2}, Cevabın: {ans})')    



    repeatTime -= 1

# POINTS
final_point = 5 + points + len(timeRecords)*5

# HIGH SCORE
try:
    ts_data = open('topScore.txt', 'r')
    top_score = ts_data.read()
except:
    open('topScore.txt','w')

try:
    top_score = int(top_score)
except:
    top_score = 0

if final_point > top_score:
    new_record = True
    top_score = final_point
    f = open('topScore.txt', 'w')
    f.write(str(top_score))
#

# AVERAGE TIME ENJOYER
sum_of_times = 0
for i in timeRecords:
    sum_of_times += i
average_time = sum_of_times/len(timeRecords)

# RESULTS
print(f"{line}\nDOĞRU CEVAP SAYISI: {len(timeRecords)}")
print(f"ORTALAMA: {round(average_time,4)} saniye")
print(f"PUAN: {final_point}/{max_points} (Başarı: %{round(final_point/max_points*100)})")
print(f"{line}\nOynadığın İçin Teşekkürler: +5\nZaman: +{points}\nDoğru Cevaplar: +{len(timeRecords)*(limit-1)*5}")
print(f'{line}\n{"YENİ REKOR!" if new_record else "Rekorunun "+str(top_score-final_point)+" puan gerisinde kaldın." }\nEN YÜKSEK PUAN: {top_score}\n{line}')


'''
 ██████╗ ██╗      █████╗ ██████╗ ██╗   ██╗██████╗ ██████╗
██╔════╝░██║░░░░░██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔══██╗
██║░░██╗░██║░░░░░██║░░██║██████╔╝██║░░░██║██║░░██║██║░░██║
██║░░╚██╗██║░░░░░██║░░██║██╔══██╗██║░░░██║██║░░██║██║░░██║
╚██████╔╝███████╗╚█████╔╝██║░░██║╚██████╔╝██████╔╝██████╔╝
 ╚═════╝ ╚══════╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝



matematik işlemi yaptıkça + para, sonra parayı kumarda yemece
kivy ile geliştir
'''