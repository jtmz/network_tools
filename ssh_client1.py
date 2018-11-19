import paramiko

host = raw_input(str('Digite o host: '))
user = raw_input(str('Digite o user: '))
passwd = raw_input(str('Digite a senha: '))

client = paramiko.SSHClient()


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    comando = raw_input('Comando: ')
    ent, ext, err = client.exec_command(comando)
    print ext.readlines()
