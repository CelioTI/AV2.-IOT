import socket
#comunicações na camada de transpote chama-se socket

HOST = ''
#variavel local

PORT = 5000
# variavel post porta udp para aceita comunicação externa

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# variavel UDP vai abrir uma porta protocolo IPV4 e um data grama

origem = (HOST, PORT)
# variavel que armazena local e porta de origem, uma estrutura chamada tuple

udp.bind(origem)
# liga as informações do host e do port

print("Serviço UDP inicializado. Aguardando mensagem. \n")
#imprimir a respota do programa


while (True):
    #loop que escuta qualquer informação que chega na porta 5000

    msg, client = udp.recvfrom(1024)
    #armazena as informações do protocolo udp

    print (client, msg)
    #imprimir resposta do loop


udp.close()
# fecha o programa
