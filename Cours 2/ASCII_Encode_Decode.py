def ascii_encode():
    phrase = input("Type your sentence here : ")
    letter = phrase.split()

    for letter in phrase:
        print(ord(letter), end=' ')

def ascii_decode():
    ascii_data = input("Enter Ascii data : ")
    list = ascii_data.split()

    for a in list:
        a = int(a)
        print(chr(a), end='')

choice = input("\nWould you like (E)ncode or (D)ecode Ascii (END to stop) : ")

while 1:
    if choice == 'E':
        ascii_encode()
    elif choice == 'D':
        ascii_decode()
    else:
        print("Thx for using this tool ! See you !")
        break

    choice = input("\nWould you like (E)ncode or (D)ecode Ascii (END to stop) : ")