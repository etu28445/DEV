txt=input("Chaine : ")
a=0
ntxt=""
while a<len(txt):
   ntxt=ntxt+(txt[a]+"*")
   a=a+1
print(ntxt)