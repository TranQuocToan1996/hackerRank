import time
start_time = time.time()

# def countApplesAndOranges(s, t, a, b, apples, oranges):
s=7
t=11
a=5
b=15
m=[-2,2,1]
n=[5,-6]
for x in apples:
        if s<=(x+a)<=t:
            apple+=1
    for x in oranges:
        if s<=(x+b)<=t:
            org+=1
    print(apple)
    print(org)
# apples=[x+a for x in m]
# oranges=[y+b for y in n]
# apple=0
# orange=0
# for applefruit in apples:
#     if s<=applefruit <=t:
#         apple+=1
# for orangefruit in oranges:
#     if s<=orangefruit<=t:
#         orange+=1
# print(apple)
# print(orange)

#other way 
# print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))

print("Process finished --- %s seconds ---" % (time.time() - start_time))