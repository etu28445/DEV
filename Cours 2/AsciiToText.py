ascii_data = input("Enter Ascii data : ")
list = ascii_data.split()

for a in list:
    a = int(a)
    print(chr(a), end='')
