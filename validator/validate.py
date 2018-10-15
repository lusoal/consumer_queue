from ast import literal_eval
from datetime import datetime
import re

def data_quality(message):
    message = message.lower()
    message = literal_eval(message)
    dicionario_itens = {}
    for key, values in message.items():
        #validando se e String ou Inteiro
        ansnum = re.match("[0-9 \-]", values)
        boolean = re.match("\b(true|false)\b", values)
        if ansnum:
            try:
                if '.' in values or ',' in values:
                    if ',' in values:
                        values = values.replace(",",".")
                    values = float(values)
                    dicionario_itens[key] = ['float', values]
                else:
                    values = int(values)
                    dicionario_itens[key] = ['int', values]
            except:
                dicionario_itens[key] = ['string', values]
                pass
        elif boolean:
            values = bool(values)
            dicionario_itens[key] = ['bool', values]
        else:
            dicionario_itens[key] = ['string', values]
    return dicionario_itens