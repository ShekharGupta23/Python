from collections import OrderedDict

d = OrderedDict([('a', 1), ('b', 2)])
d = OrderedDict({'c': 3, **d})
print(d)