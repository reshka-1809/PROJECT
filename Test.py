from random import *
a=[randint(-1000,1000) for i in range(100)]
print (a)
count=0
s=0
for q in range(100):
    if a[q]<0:
        count+=1
    else:
        s+=1
print('Положителные:',s)
print('Отрицательные:',count)
input('\n\t\tНажмите Enter для завершения ! ')
