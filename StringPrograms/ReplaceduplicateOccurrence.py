s1 = 'Gfg is best . Gfg also has Classes now. Classes help understand better .'
rep = {'Gfg': 'It', 'Classes': 'They'}
words = s1.split()
seen = set()
for i, word in enumerate(words):
    if word in rep:
        if word in seen:
            words[i] = rep[word]
        else:
            seen.add(word)
res = ' '.join(words)
print(res)