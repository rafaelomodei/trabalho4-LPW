import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='lpw',
        db='lpw',
        charset='utf8mb4',
        # cursorclass='pymysql.cursors.DictCursor'
    )

    try:
        yield conexao
    finally:
        conexao.close()


# INSERE UM REGISTRO NA BASE DE DADOS
def insert_contact(name : str, phone : str, email : str):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO agenda (nome, fone, email) VALUES ' \
                  '(%s, %s, %s)'
            cursor.execute(sql, (name, phone, email))
            conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
def insert_many_data():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO agenda (nome, fone, email) VALUES ' \
                  '(%s, %s, %s)'

            dados = [
                ('Flavio Antunes', '1845238923425', 'Flavio@meu-email.com'),
                ('Flavio Antunes', '1845238923425', 'Flavio@meu-email.com'),
                ('Flavio Antunes', '1845238923425', 'Flavio@meu-email.com'),
            ]

            cursor.executemany(sql, dados)
            conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
def delete_contact(id : int):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'DELETE FROM agenda WHERE id = %s'
            try:
                cursor.execute(sql, (id,))
                conexao.commit()
            except:
                print('Id não existente')
            finally:
                print('Sucesso')


# DELETA QUANTIDADE DETERMINADA DE REGISTROS
def delete_many_contacts(first_id : int, second_id : int):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'DELETE FROM agenda WHERE id IN (%s, %s)'
            cursor.execute(sql, (first_id, second_id))
            conexao.commit()

# DELETA REGISTRA ENTRE UM RANGE
def delete_in_range_contacts(first_id : int, last_id : int):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'DELETE FROM agenda WHERE id BETWEEN %s AND %s'
            cursor.execute(sql, (first_id, last_id))
            conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
def update_contact(id: int, new_name : str = None, new_phone: str = None, new_email : str = None):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            try:
                if(new_name != None):
                    sql = 'UPDATE agenda SET nome=%s WHERE id=%s'
                    cursor.execute(sql, (new_name, id))
                if(new_phone != None):
                    sql = 'UPDATE agenda SET fone=%s WHERE id=%s'
                    cursor.execute(sql, (new_phone, id))
                if (new_email != None):
                    sql = 'UPDATE agenda SET email=%s WHERE id=%s'
                    cursor.execute(sql, (new_email, id))
                if (new_name == None and new_phone == None and new_email == None):
                    print('Nada pode ser modificado')
                conexao.commit()
            except:
                print('Id não existente')
            finally:
                print('Operacao realizada')

# INSERIR DADOS QUE SÃO SOLICITADOS AO USUÁRIO
def insert_inputed_contact():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            nome = input('Informe seu nome: ')
            fone = int(input('Informe seu número de telefone: '))
            email = input('Informe seu email: ')

            sql = 'INSERT INTO agenda (Nome, Fone, Email)  VALUES ' \
                  '(%s, %s, %s)'
            cursor.execute(sql, (nome, fone, email))
            conexao.commit()

# DELETAR DADOS QUE SÃO SOLICITADOS AO USUÁRIO
def delete_inputed_contact():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            id = int(input('Digite o id do usuário a ser removido: '))
            delete_contact(id)

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
def show_all_contacts():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT id, nome, fone, email FROM agenda ORDER BY nome ASC LIMIT 100')
            resultado = cursor.fetchall()

            for linha in resultado:
                print(linha)

def update_inputed_contact():
    id = int(input('Id do contato a ser modificado: '))
    print('Caso resposta seja vazia, permanecerá o mesmo valor')
    name = input('Nome novo: ') or None
    phone = input('Novo fone: ') or None
    email = input('Novo email: ') or None

    update_contact(id, name, phone, email)