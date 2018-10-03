# -*- coding: utf-8 -*-
import yaml

from fila.testingfila import * 
from validator.validate import *
from database.mysql_insert import * 

def callback(ch, method, properties, body):
    #tudo dentro do Callback pois é um Worker
    message_formatted = data_quality(body)
    querie = define_querie(message_formatted)
    print (querie)
    #inserir no database

def main():
    channel = connect_to_rabbit(configs)
    channel.basic_consume(callback,queue='messages',no_ack=True)
    
    #inicia a Daemon
    channel.start_consuming()

if __name__ == "__main__":
    main()