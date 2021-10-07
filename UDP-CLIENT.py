import socket
# comunicações na camada de transpote chama-se socket

HOST = 'localhost'
#variavel local
PORT = 5000
# variavel post porta udp pra pra aceita comunicação externa

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# variavel UDP vai abrir uma porta protocolo IPV4 e um data grama
destino = (HOST, PORT)
# variavel onde amazena a mensagem final

while (True):
    mensagem = bytes(input('Digite a mensagem:  '), encoding='utf-8')
    #codigo de entrada de informação, transforma a informação de str em bytes
    udp.sendto(mensagem, destino)
    #envia a mensagem do cogigo acima para o destino (HOST, PORT)

udp.close()
# fecha o programa