list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

list3 = []

for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(list3)