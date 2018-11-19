import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
try:
    client.connect(("jtmz.com.br", 80))
    client.send("GET / HTTP/1.1\nHost: jtmz.com.br\n\n\n")

    pacotes_recebidos = client.recv(1024)

    print pacotes_recebidos

except:
    print "Conexao Falhou"
