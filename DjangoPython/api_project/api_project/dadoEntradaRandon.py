#Necessario ter instalado a biblioteca
        #pip install paho-mqtt

#Import das bibliotecas
import random
import time
import json
import paho.mqtt.client as mqtt

# Configurações do broker MQTT
broker_address = 'localhost'
broker_port = 1883 #Porta do Docker

# Configurações do tópico e número de mensagens
topic = 'dados_entrada'
num_messages = 100

# Função para quando a conexão com o broker for estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT")
    client.subscribe(topic)

# Função de callback para quando uma mensagem é publicada com sucesso
def on_publish(client, userdata, mid):
    print(f"Mensagem publicada com sucesso: {mid}")

# Criação do cliente MQTT
client = mqtt.Client()

# Configuração dos callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# Conexão com o broker MQTT
client.connect(broker_address, broker_port)

# Loop principal
client.loop_start()

# Envio das mensagens
for i in range(num_messages):
    data_entry = {
        'valor': random.uniform(0, 10),
        'data_hora': time.strftime('%Y-%m-%dT%H:%M:%S')
    }
    payload = json.dumps(data_entry)
    client.publish(topic, payload)
    time.sleep(1)

# Aguarda as mensagens serem enviadas antes de encerrar
time.sleep(2)

# Encerramento do cliente MQTT
client.loop_stop(100)
client.disconnect()
