import random
a = []
for b in range(int(input("num de veces: "))):
    a.append(random.randint(0,2))

print("1: ", a.count(0))
print("2: ", a.count(1))
print("3: ", a.count(2))