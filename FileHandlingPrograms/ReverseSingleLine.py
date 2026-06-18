with open('gfg.txt', 'r') as f:
    lines = f.readlines()  

choice = 0 

line = lines[choice].split()  
lines[choice] = " ".join(line[::-1]) + "\n"  

with open('gfg.txt', 'w') as f:
    f.writelines(lines)