from textwrap import wrap

s1 = "qsdfghjtghujkefds;jgnrlerngl"
s2 = ""

while s1:
    s2 = s1[:5] + s2
    s1 = s1[5:]
print(s2)


s1 = "qsdfghjkklmdfghjkklfgbhnj"
s2 = ""

print(wrap(s1, 5))

for s in wrap(s1, 5):
    s2 = s + s2
