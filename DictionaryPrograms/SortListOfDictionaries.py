from operator import itemgetter

d = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19}
]
print("Sorted by age: ",sorted(d, key=itemgetter('age')))