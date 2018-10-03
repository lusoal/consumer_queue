from ast import literal_eval    

def data_quality(message):
    message = message.lower()
    message = literal_eval(message)
    
    #Redirecionar para Log print (type(message))
    
    return message
    #validar tambem se a quantidade de campos cadastrados esta correta, se nao descartar o dado
    #verificar possibilidade do que fazer caso os campos estejam errados
    #validar se as colunas do mysql batem com os items dos DICT