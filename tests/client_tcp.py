import socket
HOST = '10.7.124.30'     # Endereco IP do Servidor
PORT = 5354           # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = raw_input()
while msg != ('\x18'):
    tcp.send (msg)
    msg = raw_input()
tcp.close()