import yaml

configs = yaml.load(open('config.yml'))

def define_querie(value):
    querie = "INSERT INTO {} VALUES(".format(configs['database']['table_name'])
    for key, value in value.items():
        querie+=str("'{}',".format(value))
    querie+=")"
    querie = (querie[:-2]+")")
    return querie