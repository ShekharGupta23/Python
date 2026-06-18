import shutil

with open('file2.txt', 'r') as f2, open('file1.txt', 'a') as f1:
    shutil.copyfileobj(f2, f1)