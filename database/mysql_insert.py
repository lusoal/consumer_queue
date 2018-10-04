import yaml

configs = yaml.load(open('config.yml'))

def define_querie(value):
    table_name = None

    #verificar em qual tabela ira inserir o dado parseado
    if "clientes" in value['table_name']:
        table_name = "clientes"
    else:
        table_name = "transacoes"
    
    value.pop('table_name', None)
    querie = "INSERT INTO {} VALUES(".format(table_name)
    for key, value in value.items():
        querie+=str("'{}',".format(value))
    querie+=")"
    querie = (querie[:-2]+")")
    return querie