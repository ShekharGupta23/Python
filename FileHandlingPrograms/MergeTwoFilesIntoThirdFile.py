with open('merged_file.txt', 'w') as outfile:
    for filename in ['file1.txt', 'file2.txt']:
        with open(filename, 'r') as infile:
            outfile.write(infile.read())  
            outfile.write('\n')