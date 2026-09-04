with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for ln, line in enumerate(infile, 1):
        if ln % 2 != 0: 
            outfile.write(line)