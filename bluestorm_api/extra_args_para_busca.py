


def get_patients_args(args):
    f_n = args.get('first_name', default='', type=str)
    return f_n


def get_pharmacies_args(args):
    n = args.get('name', default='', type=str)
    return n


def get_transactions_args(args):
    pa_first_name, ph_name = args.get('pa_first_name', default='', type=str), args.get('ph_name', default='', type=str)
    return pa_first_name, ph_name