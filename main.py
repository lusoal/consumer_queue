# -*- coding: utf-8 -*-
import yaml

from fila.testingfila import * 
from validator.validate import *
from database.mysql_insert import * 

def callback(ch, method, properties, body):
    #tudo dentro do Callback pois é um Worker
    body = body.decode("utf-8")
    #decript byte to string
    
    message_formatted = data_quality(body)
    querie = define_querie(message_formatted)
    
    retorno = sql_insert_into_db(querie)
    if retorno == True:
        print (retorno)
        ch.basic_ack(delivery_tag=method.delivery_tag, multiple=False)
    #inserir no database

def main():
    channel = connect_to_rabbit(configs)
    channel.basic_qos(prefetch_count=1)
    result = channel.basic_consume(callback,queue='messages',no_ack=False)
    print (result)
    #
    #inicia a Daemon
    channel.start_consuming()
    channel.close()

if __name__ == "__main__":
    main()