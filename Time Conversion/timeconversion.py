import time
start_time = time.time()
s='07:05:45PM'
# AMPM=s[-2:]
# if s[0:2]=='12' and AMPM=='AM':
#     print('00'+s[2:8])
# elif AMPM=='PM':
#     print(str(int(s[0:2])+12)+s[2:8])
# else:
#     print(s[:8])

# other way

AM_PM = s[-2:]
s = s[:8]
hh, mm, ss = [int(x) for x in s.split(":")]

if AM_PM == 'PM' and hh != 12:
    print('{:02}:{:02}:{:02}'.format(hh+12, mm, ss))
elif AM_PM == 'AM' and hh == 12:
    print('{:02}:{:02}:{:02}'.format(0, mm, ss))
else:
    print('{:02}:{:02}:{:02}'.format(hh, mm, ss))

print("Process finished --- %s seconds ---" % (time.time() - start_time))





