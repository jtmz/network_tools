import ipaddress

ip = u'192.168.0.100/24'

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print ip
