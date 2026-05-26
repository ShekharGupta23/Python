from functools import reduce

t = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
l = ['Geeks', 'best', 'CS', 'Gfg']

res = reduce(lambda acc, key: acc + [ele for ele in t if ele[0] == key], l, [])
print( res)