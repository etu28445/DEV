import base64
def b64_encode():
    phrase = input("Type your sentence here : ")
    x = base64.b64encode(bytes(phrase, 'utf-8'))
    print(x.decode())

def b64_decode():
    b64_str = input("Enter Ascii data : ")
    y = base64.b64decode(bytes(b64_str, "utf-8"))
    print(y.decode())

choice = input("\nWould you like (E)ncode or (D)ecode your string in Base64 (END to stop) : ")

while 1:
    if choice == 'E':
        b64_encode()
    elif choice == 'D':
        b64_decode()
    else:
        print("Thx for using this tool ! See you !")
        break

    choice = input("\nWould you like (E)ncode or (D)ecode your string in Base64 (END to stop) : ")