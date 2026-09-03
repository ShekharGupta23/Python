class Stack:
    def __init__(self):
        self._arr = [] 

    def push(self, val):
        self._arr.append(val)  

    def pop(self):
        if self.is_empty():
            return None
        return self._arr.pop()  

    def is_empty(self):
        return len(self._arr) == 0  

def reverse_file(filename):
    S = Stack()
    
    with open(filename, 'r') as original:
        for line in original:
            S.push(line.rstrip("\n"))

    with open(filename, 'w') as output:
        while not S.is_empty():
            output.write(S.pop() + "\n")

filename = "file.txt"
reverse_file(filename)

with open(filename) as file:
    for f in file.readlines():
        print(f, end="")