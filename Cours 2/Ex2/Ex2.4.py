list = [1,2,3,4,5]

pair = []
impair = []

for n in list:
    if n % 2 == 0:
        pair.append(n)
    else:
        impair.append(n)

print(pair)
print(impair)