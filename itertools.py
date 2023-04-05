# itertools.py
import itertools

def first_letter (name):
    # print (name[0])
    return name[0]

names = ["Tania","Farras","Faris","Noah"]

for letter , name_grouped in itertools.groupby(names, first_letter):
    print (letter, list(name_grouped))

# T ['Tania']
# F ['Farras', 'Faris']
# N ['Noah']