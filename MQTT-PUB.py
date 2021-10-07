import paho.mqtt.client as mqtt
# importou a biblioteca paho com o apilido mqtt

BROKER = "loclhost"
# variavel para diferenciar HOST

PORT = 1883
# porta de conexão 

client = mqtt.Client('pub-py')
# variavel vai receber a class mqtt.Client

client.connect(BROKER, PORT)
#conexão ao servidor e a porta 1883

def on_publish_callback(client, userdata, result):
#função vai mostra quando os dados foram publicados

    print("Dado publicado")
    #imprimir resposta da função

client.on_publish = on_publish_callback
# exercuta quando o dado e publicado

status = "false"
#vai inicializa como false e depois utiliza os valores dentro do while


while(True):
#loop
    value = input('Digite 1 para ou 0 para desliga:  ')
    #onde o usuario entra com as opções
    if(value == "0"):
    #bloco de decisão baixo nivel
        status = "false"
        #se o valor for 0 vai escreve desligado
    elif(value == "1"):
    #bloco de decisão alto nivel
        status = "True"
        #se o valor for 1 vai escreve ligado

client.publish('casa/sala/lampada/1','{"status": %s }' % status)
#vai publica a mensagem de fato

print ('{"status":  %s status}')
#imprimir status