import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 80
file = open("shell.php", 'w')

try:
    server.bind((ip, port))
    server.listen(5)
    print "Listening in: " +ip+ ":" + str(port)

    (client_socket, address) = server.accept()
    print "Received from: " + address[0]

    while True:

        data = client_socket.recv(1024)
        if data == "cd123\n":

            client_socket.send("ACK")
            print("0")
            server.close()
        else:


            client_socket.send("NOT FOUND")

            server.close()

except Exception as erro:
    print "Erro: " + str(erro)
    server.close()
