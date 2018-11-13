import yaml
from sqlalchemy import *
from sqlalchemy.orm import *

configs = yaml.load(open('config.yml'))

def define_querie(value):
    table_name = None
    columns = ""
    #verificar em qual tabela ira inserir o dado parseado
    if "clientesparceiros" in value['table_name'][1]:
        table_name = "clientesparceiros"
    elif "quantidadeparceiros" in value['table_name'][1]:
        table_name = "quantidadeparceiros"
    elif "vendaparceiros" in value['table_name'][1]:
        table_name = "vendaparceiros"
    elif "clientespotenciais" in value['table_name'][1]:
        table_name = "clientespotenciais"
    else:
        table_name = "aeroportos"
    value.pop('table_name', None)
    for k, v in value.items():
        #remover \n do cabecalho
        if k[-1:-2:-1] == '\n':
             k = k.strip()
        columns += "{},".format(k)
    querie = "INSERT INTO {} ({}) VALUES(".format(table_name, columns[:-1])
    for key, val in value.items():
        if val[0] == "string" or val[0] == "bool":
            querie+=str("'{}',".format(val[1]))
        elif val[0] == "int" or val[0] == "float":
            querie+=str("{},".format(val[1]))
    querie+=")"
    querie = (querie[:-2]+")")
    return querie



#Use this if u are using SqlAlchemy
def sql_insert_into_db(query):
    print (query)
    #connection db
    engine = create_engine("mysql://{}:{}@{}/{}".format(configs['database']['user'],configs['database']['pass'],configs['database']['host'], configs['database']['schema']))
    #creating session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    stmt = query
    try:
        result_proxy = session.execute(stmt)
        if 'INSERT' in stmt or 'UPDATE' in stmt or 'DELETE' in stmt:
            session.commit()
            return True
        if 'SELECT' in stmt:
            result = result_proxy.fetchall()
            return result
    except Exception as e:
        print  (e)
        if '_mysql_exceptions.IntegrityError' in str(e):
            return False
            print ("Ja inserido")
        else:
            return False