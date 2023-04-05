from time import time

list_1 = [1,2,3,4,5]
list_2 = [[a for a in range (1,100)] for a in range (1,1000000)]

now = time()
gabungan = []

for chunk in list_2:
    #print(chunk)
    list_1+chunk

# print(list_2)
print("Estimasi : {:.4f} ".format(time() - now))
now2 = time()

for chunk in list_2:
    list_1.extend(chunk)

print("Estimasi Extend : {:.4f}".format(time() - now2))
