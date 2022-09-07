

def patients_data_to_json(rows):
    to_dict = {}
    for row in rows:
        to_dict.update({ row[0] : {} })
        to_dict[row[0]].update({ 'ID' : row[0] })
        to_dict[row[0]].update({ 'Nome' : row[1] })
        to_dict[row[0]].update({ 'Sobrenome' : row[2] })
        to_dict[row[0]].update({ 'Data de nascimento' : row[3] })
    return to_dict
        


def pharmacies_data_to_json(rows):
    to_dict = {}
    for row in rows:
        to_dict.update({ row[0] : {} })
        to_dict[row[0]].update({ 'ID' : row[0] })
        to_dict[row[0]].update({ 'Nome' : row[1] })
        to_dict[row[0]].update({ 'Cidade' : row[2] })
    return to_dict


def trasactions_information_to_json(rows):
    to_dict = {}
    for row in rows:
        to_dict.update({ row[7] : {} })
        to_dict[row[7]].update({ 'ID do paciente' : row[0] })
        to_dict[row[7]].update({ 'nome do paciente' : row[1] })
        to_dict[row[7]].update({ 'sobrenome do paciente' : row[2] })
        to_dict[row[7]].update({ 'data de nascimento do paciente' : row[3] })
        to_dict[row[7]].update({ 'ID da farmácia' : row[4] })
        to_dict[row[7]].update({ 'nome da farmácia' : row[5] })
        to_dict[row[7]].update({ 'cidade da farmácia' : row[6] })
        to_dict[row[7]].update({ 'ID da transação' : row[7] })
        to_dict[row[7]].update({ 'quantidade da transação' : row[8] })
        to_dict[row[7]].update({ 'data da transação' : row[9] })
    return to_dict

def get_one_user(row):
    to_dict = {'Error': 'User with these credentials does not exist.'}
    for r in row:
        to_dict = {}
        to_dict.update({ 'uuid': r[0] })
        to_dict.update({ 'username': r[1] })
        to_dict.update({ 'password': r[2] })
        break
    return to_dict

