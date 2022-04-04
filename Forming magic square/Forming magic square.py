
import time
start_time = time.time()

from itertools import permutations
s=[]
a=[]
b=[]
minus=[]
sum=0
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
for row in s:
    for number in row:
        a.append(number)
perm = permutations((1,2,3,4,5,6,7,8,9))
for i in list(perm):
    if (i[0]+i[1]+i[2]==15) and  (i[3]+i[4]+i[5]==15) and (i[6]+i[7]+i[8]==15) and (i[0]+i[3]+i[6]==15) and (i[1]+i[4]+i[7]==15) and (i[2]+i[5]+i[8]==15) and (i[0]+i[4]+i[8]==15) and (i[2]+i[4]+i[6]==15):      
        b.append(i)
for i1 in b:
    for i2 in range(9):
        sum+=abs(a[i2]-i1[i2])
    minus.append(sum)
    sum=0
print(min(minus))

print("Process finished --- %s seconds ---" % (time.time() - start_time))