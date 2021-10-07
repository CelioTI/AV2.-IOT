import socket
#comunicações na camada de transpote chama-se socket

HOST = ''
#variavel local

PORT = 5000
# variavel post porta udp para aceita comunicação externa

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# variavel TCP vai abrir uma porta protocolo IPV4 e reponsavel por abri no TCP

origem = (HOST, PORT)
# variavel que armazena local e porta de origem, uma estrutura chamada tuple

tcp.bind(origem)
# liga as informações do host e do port

tcp.listen(1)
# informa quantas conexão por vez ele pode ouvir

print ('Serviço iniciado. ')
#imprimir respota do programa

while(True):
    #esse loop via estabelece a conexão

    con, client = tcp.accept()
    # cria uma conexão entre os dois  e começa a receber as informações do outro lado 


    print('Conectando por ', client)
    #imprimir respota do loop

    while(True):
    #esse loop vai recebe os dados

        mensagem = con.recv(1024)
        # essa variavel vai exibir os dados

        print(client, mensagem)
        #imprimir respota do loop

    con.closer()
    #fecha o loop
    
con.closer()
#fecha o loop