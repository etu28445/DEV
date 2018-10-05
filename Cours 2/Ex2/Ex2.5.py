list = ["Jean", "Maximilien", "Brigitte", "Sonia", "Jean-Pierre", "Sandra"]

less6 = []
more6 = []

for name in list:
    if len(name) < 6:
        less6.append(name)
    else:
        more6.append(name)

print(less6)
print(more6)