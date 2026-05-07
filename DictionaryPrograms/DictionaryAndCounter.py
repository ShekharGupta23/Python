from collections import Counter
votes = ['john','johnny','jackie','johnny','john','jackie', 'jamie','jamie','john','johnny','jamie','johnny','john']
c = Counter(votes)
m = max(c.values())
w = [i for i in c if c[i] == m]
print(sorted(w)[0])