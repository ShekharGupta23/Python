from collections import OrderedDict

s = 'engineers rock'
p = 'er'
od = OrderedDict.fromkeys(s)
ptr = 0

for k in od:
    if k == p[ptr]:
        ptr += 1
    if ptr == len(p):
        print(True)
        break
else:
    print(False)