import pymysql.cursors
import json


def list_alunos():
    db_host="database-2.cxme3nonyefk.us-east-1.rds.amazonaws.com"
    db_banco="bancodevmobile"
    
    listaAluno =[]
    jsonAluno = {}
    
    
    # Connect to the database
    connection = pymysql.connect(host=db_host,
                                user='admin',
                                password='gabriel061294',
                                database=db_banco,
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        #with connection.cursor() as cursor:
            #sql = "INSERT INTO aluno (nome, telefone) VALUES (%s, %s)"
            #cursor.execute(sql)

        #connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT nome FROM aluno"
            cursor.execute(sql)
            registros = cursor.fetchall()
            for aluno in registros:
                listaAluno.append(aluno["nome"])
    
    #monta o json de saida
    jsonAluno["alunos"] = listaAluno
    json_object = json.dumps(jsonAluno, indent=4 ) 
    
    return json_object    