import json
from contests.models import ModxDbimgMuz as muz


def load_json(path_name):
    with open(path_name, 'r', encoding='utf-8') as fh:
        result = json.load(fh)
    return result


def get_data():
    muz.objects.using('vm').all().last()
