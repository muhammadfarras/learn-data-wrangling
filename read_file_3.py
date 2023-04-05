files = "read_file_2.txt"

f1 = open(files, encoding="utf-8")
f2 = open(files,  mode="rb")

print(f1.read(10))
# My_ñam_is_ (10 karakter)

print(f2.read(10))
# b'My_\xc3\xb1am_is'

print(f1.tell())

print(f2.tell())