from datetime import datetime
from itertools import islice


def get_retrieve_data(uploadfile):
    data = [row for row in islice(uploadfile, 1, None) if '' not in row[:2]]
    data = get_validation(data)
    return data


def get_validation(data):
    for row in data:
        row[3] = check_decimal(row[3])
        row[2] = check_num(row[2])
        row[4] = check_date(row[4])
        row[5:] = check_services(row[5:])
    data = [row for row in data if False not in row[2:]]
    return data


def check_num(value):
    try:
        if isinstance(value, float):
            return False
        value = int(value)
        if value <= 0:
            return False
        return value
    except ValueError:
        return False


def check_decimal(value):
    try:
        if isinstance(value, int):
            return float(format(value, '.2f'))
        if isinstance(value, float):
            return float(format(value, '.2f'))
        else:
            value = float(value.replace(',', '.'))
            value = float(format(value, '.2f'))
            return value
    except ValueError:
        return False


def check_date(value):
    try:
        if '.' in value:
            value = str(datetime.strptime(value, '%d.%m.%Y').date())
        if ',' in value:
            value = str(datetime.strptime(value, '%d,%m,%Y').date())
        return value
    except ValueError:
        return False


def check_services(values):
    values = [row.strip() for row in values if row not in ('', '-')]
    if values:
        return values
    return [False]
