import socket

client_connect = raw_input('Set ip or domain for scanning: ')
ports = [21, 22, 23, 24, 25, 80, 135, 143, 443, 3306, 8080]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.6)

    code = client.connect_ex((client_connect, port))

    if code == 0:
        print str(port) + " - Port Open, Connection acepted"

print "Finished Scan"
