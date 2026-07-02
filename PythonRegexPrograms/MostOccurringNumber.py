import re
from collections import Counter
s = 'geek55of55gee4ksabc3dr2x'
a = re.findall(r'\d+', s)
freq = Counter(a)
res = max(freq, key=lambda x: (freq[x], int(x)))
print(res)