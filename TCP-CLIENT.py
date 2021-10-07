import socket
#comunicações na camada de transpote chama-se socket

HOST = 'localhost'
# faz a conexão com o servidor TCP

PORT = 5000
# variavel post porta udp para aceita comunicação externa

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# variavel TCP vai abrir uma porta protocolo IPV4 e reponsavel por abri no TCP

destino = (HOST, PORT)
# variavel que armazena local e porta de destino, uma estrutura chamada tuple

tcp.connect(destino)
#estabele uma conexão com o destino

while(True):
    #loop
    mensagem = bytes(input('Digite a mensagem:  '), encoding='utf-8')
    #codigo de entrada de informação do cliente, transforma a informação de str em bytes

    tcp.send(mensagem)
    # manda as mensagens do client

tcp.close()
#fecha o programa