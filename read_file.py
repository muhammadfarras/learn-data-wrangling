filename="read_file_1.txt"
f = open(filename, encoding="utf-8")

for a in f:
    print (a)

f.close()