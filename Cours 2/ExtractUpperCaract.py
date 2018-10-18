phrase = "Test1 test2 Test3 Allo Comment va Tu"

words = phrase.split()

for word in words:
    if(word[0].isupper()):
        print(word)

