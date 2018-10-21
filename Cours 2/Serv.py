import socket
import subprocess, sys

TCP_IP = '10.0.1.5'
PORT = 64698
BUFFER_SIZE = 1024
PASS = b'123'


#############################################################
def Login():
    whoareyou = b"Login : "
    connection.send(whoareyou)
    pwd = connection.recv(BUFFER_SIZE)

    if pwd.strip() != PASS:
        Login()
    else:
        shell_msg = bytes("You have a shell ! #> ", "utf-8")
        connection.send(shell_msg)
        Shell()


#############################################################
def Shell():
    while True:
        data = connection.recv(BUFFER_SIZE)
        if data:
            for i in data:
                data_dec = data.decode("utf-8")

            if data_dec == "FIN":
                msg = b"Connection closed by client !\n"
                msg_dec = msg.decode("utf-8")
                print(msg_dec, client_address)
                connection.send(b"Client Disconnected")
                connection.send(msg)
                break

            #p = subprocess.Popen(data_dec, stdout=subprocess.PIPE, shell=True)

            with open('test.log', 'w') as f:
                p = subprocess.Popen(data_dec, stdout=subprocess.PIPE, shell=True)
                for line in iter(p.stdout.readline, ''):
                    line_str = str(line)
                    sys.stdout.write(line_str)
                    f.write(line_str)
                    f.flush()
                    connection.send(line)
                    
                    if line == b"":
                        connection.recv(BUFFER_SIZE)
                        break

                p_status = p.wait()
                print("Command output : ", output)
                print("Command exit status/return code : ", p_status)
                if p_status == 1:
                    x = b'Wrong Command...\n\n'
                    connection.send(x)
                else:
                    x = b'Success\n\n'
                    connection.send(x)

                f.close()

            
            """(output, err) = p.communicate()
            p_status = p.wait()
            print("Command output : ", output)
            print("Command exit status/return code : ", p_status)
            line = ""
            for line in iter(p.stdout.readline, b''):  # replace '' with b'' for Python 3
                sys.stdout.write(line)
                sys.stdout.flush()
                #connection.send(output)
                #print(data_dec)
                if p_status == 1:
                    x = b'Wrong Command...\n\n'
                    connection.send(x)
                else:
                    x = b'Success\n\n'
                    connection.send(x)"""
                
                
                

        else:
            print("no more data.")
            break


##################################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP_IP socket
local_hostname = socket.gethostname()  # local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname

print("working on ", local_hostname, " (", local_fqdn, ") with ", TCP_IP)

server_address = (TCP_IP, PORT)

print("starting up on ", server_address, " port ", PORT)

sock.bind(server_address)
sock.listen(1)

# put sock accept here -> won't continue to listen


while 1:

    print('waiting for a connection ... ')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        Login()

    finally:
        connection.close()
