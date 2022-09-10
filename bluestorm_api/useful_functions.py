"""Auxiliary functions for the bluestorm_api.sqlite_db module"""


def patients_data_to_json(rows):
    """Função percorre uma variável do tipo Cursor.
       Retorna um dict com os dados do Cursor ou com uma mensagem de erro."""
    row = rows.fetchone()
    if row:
        to_dict = {}
        to_dict.update({row[0] : {}})
        to_dict[row[0]].update({'ID' : row[0]})
        to_dict[row[0]].update({'NOME' : row[1]})
        to_dict[row[0]].update({'SOBRENOME' : row[2]})
        to_dict[row[0]].update({'DATA DE NASCIMENTO' : row[3]})
    else:
        to_dict = {'ERROR': 'NO DATA FOUND'}
    for row in rows:
        to_dict.update({row[0] : {}})
        to_dict[row[0]].update({'ID' : row[0]})
        to_dict[row[0]].update({'NOME' : row[1]})
        to_dict[row[0]].update({'SOBRENOME' : row[2]})
        to_dict[row[0]].update({'DATA DE NASCIMENTO' : row[3]})
    return to_dict


def pharmacies_data_to_json(rows):
    """Função percorre uma variável do tipo Cursor.
       Retorna um dict com os dados do Cursor ou com uma mensagem de erro."""
    row = rows.fetchone()
    if row:
        to_dict = {}
        to_dict.update({row[0] : {}})
        to_dict[row[0]].update({'ID' : row[0]})
        to_dict[row[0]].update({'NOME' : row[1]})
        to_dict[row[0]].update({'CIDADE' : row[2]})
    else:
        to_dict = {'ERROR': 'NO DATA FOUND'}
    for row in rows:
        to_dict.update({row[0] : {}})
        to_dict[row[0]].update({'ID' : row[0]})
        to_dict[row[0]].update({'NOME' : row[1]})
        to_dict[row[0]].update({'CIDADE' : row[2]})
    return to_dict


def trasactions_information_to_json(rows):
    """Função percorre uma variável do tipo Cursor.
       Retorna um dict com os dados do Cursor ou com uma mensagem de erro."""
    row = rows.fetchone()
    if row:
        to_dict = {}
        to_dict.update({row[7] : {}})
        to_dict[row[7]].update({'ID DO PACIENTE' : row[0]})
        to_dict[row[7]].update({'NOME DO PACIENTE' : row[1]})
        to_dict[row[7]].update({'SOBRENOME DO PACIENTE' : row[2]})
        to_dict[row[7]].update({'DATA DE NASCIMENTO DO PACIENTE' : row[3]})
        to_dict[row[7]].update({'ID DA FARMACIA' : row[4]})
        to_dict[row[7]].update({'NOME DA FARMACIA' : row[5]})
        to_dict[row[7]].update({'CIDADE DA FARMACIA' : row[6]})
        to_dict[row[7]].update({'ID DA TRANSACAO' : row[7]})
        to_dict[row[7]].update({'QUANTIDADE DA TRANSACAO' : str(row[8])})
        to_dict[row[7]].update({'DATA DA TRANSACAO' : row[9]})
    else:
        to_dict = {'ERROR': 'NO DATA FOUND'}
    for row in rows:
        to_dict.update({row[7] : {}})
        to_dict[row[7]].update({'ID DO PACIENTE' : row[0]})
        to_dict[row[7]].update({'NOME DO PACIENTE' : row[1]})
        to_dict[row[7]].update({'SOBRENOME DO PACIENTE' : row[2]})
        to_dict[row[7]].update({'DATA DE NASCIMENTO DO PACIENTE' : row[3]})
        to_dict[row[7]].update({'ID DA FARMACIA' : row[4]})
        to_dict[row[7]].update({'NOME DA FARMACIA' : row[5]})
        to_dict[row[7]].update({'CIDADE DA FARMACIA' : row[6]})
        to_dict[row[7]].update({'ID DA TRANSACAO' : row[7]})
        to_dict[row[7]].update({'QUANTIDADE DA TRANSACAO' : str(row[8])})
        to_dict[row[7]].update({'DATA DA TRANSACAO' : row[9]})
    return to_dict


def get_one_user(row):
    """Função percorre uma variável do tipo Cursor.
    Retorna um dict com os dados do Cursor ou com uma mensagem de erro."""
    user_row = row.fetchone()
    if user_row:
        to_dict = {}
        to_dict.update({'uuid': user_row[0]})
        to_dict.update({'username': user_row[1]})
        to_dict.update({'password': user_row[2]})
    else:
        to_dict = {'ERROR': 'USER WITH THESE CREDENTIALS DOES NOT EXIST'}
    return to_dict
