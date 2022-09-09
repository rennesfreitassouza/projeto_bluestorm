"""Auxiliary functions for the bluestorm_api.bluestorm_api module"""


def get_patients_args(args):
    """Utiliza o método do módulo Flask request.args.get() para extrair uma str
       do parâmetro first_name da URL e retorna essa str."""
    f_n = args.get('first_name', default='', type=str)
    return f_n


def get_pharmacies_args(args):
    """Utiliza o método do módulo Flask request.args.get() para extrair uma str
       do parâmetro name da URL e retorna essa str."""
    nome = args.get('name', default='', type=str)
    return nome


def get_transactions_args(args):
    """Utiliza o método do módulo Flask request.args.get() para extrair duas str
       dos parâmetros pa_first_name e ph_name da URL e retorna uma tupla com
       essas str."""
    pa_first_name, ph_name = args.get('pa_first_name', default='',
                 type=str), args.get('ph_name', default='', type=str)
    return pa_first_name, ph_name
