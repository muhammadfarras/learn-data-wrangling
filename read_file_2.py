filename = "read_file_1.txt"

with open(filename, encoding="utf-8") as f:
    line = [x.rstrip() for x in f]

print(line)