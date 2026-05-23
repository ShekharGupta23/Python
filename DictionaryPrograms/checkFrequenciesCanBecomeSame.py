from collections import Counter

s = 'xxxyyzzt'

freq = Counter(s)
same = list(set(freq.values()))

if len(same) > 2:
    print('No')
elif len(same) == 2 and abs(same[1] - same[0]) > 1:
    print('No')
else:
    print('Yes')