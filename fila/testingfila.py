import pika
import yaml

#load das configuracoes
configs = yaml.load(open('config.yml'))

def connect_to_rabbit(configs):
    retorno = False
    try:
        credentials = pika.PlainCredentials(configs['rabbit']['user'], configs['rabbit']['pass'])
        params = pika.ConnectionParameters(configs['rabbit']['host'], configs['rabbit']['port'], '/', credentials)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        retorno = channel
    except Exception as e:
        print (e)
    return retorno
