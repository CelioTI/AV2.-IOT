import paho.mqtt.client as mqtt
# importou a biblioteca paho com o apilido mqtt

import json
#importa a biblioteca json

client = mqtt.Client(client_id='sub-py')
# instanciando um class client

client.connect('localhost', port=1883)
# cliente faz uma conexão ao broker

client.subscribe('casa/sala/lampada/1')
#topico e uma esquema de caminho para recursos de um determindo servidor

print("Subscriber connected!")
#imprimir resposta

def on_message_callback(client, userdata, message):
# função vai receber os dados da mensagem e imprimir
    msg = json.loads(message.payload.decode('utf-8'))
    
    if(msg["status"] == True):
    #bloco de decição caso for True 'pino ligado
        print("Pino X ligado")
        #imprimir resposta
    elif(msg["status"] == False):
    # bloco de decição caso for False 'pino deligado
        print("Pino X desligado")
        #imprimir resposta

client.on_message = on_message_callback
# chega a mensagem e ele exercuta o callback tira um print no payload

client.loop_forever()
#loop eterno do client     