import xlrd
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from mailing.models import Subscriber, GroupSubscribe


def parse_xls(path_file, group_subscribe):
    result = []
    rb = xlrd.open_workbook(path_file)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        phone_number = None
        row = sheet.row_values(rownum)
        try:
            email = str(row[0].replace(' ', '')).lower()
            validate_email(email)
        except ValidationError:
            continue
        group = GroupSubscribe.objects.get(id=group_subscribe)

        if len(row) == 2:
            phone_number = ''.join([i for i in str(row[1]) if i.isdigit()])
            if phone_number:
                phone_number = '8' + phone_number[1:] if phone_number[
                                                             0] == '7' else phone_number
                phone_number = '8' + phone_number if phone_number[
                                                         0] == '9' else phone_number
                phone_number = phone_number[:11] if len(
                    phone_number) > 11 else phone_number
        result.append(
            {'email': email, 'group': group, 'phone_number': phone_number})
    if result:
        return result
    else:
        return None
