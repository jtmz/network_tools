import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:


    while True:
        client.sendto(raw_input("Voce: ") + "\n", ("127.0.0.1", 666))

        msg, receiver = client.recvfrom(1024)

        print receiver[0] + ": " + msg

    client.close()

except Exception as erro:
    print "Conexao Falhou"
    print erro
    client.close()
