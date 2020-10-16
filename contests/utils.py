import time


def generate_year():
    if int(time.strftime('%m', time.localtime())) < 7:
        year_contest = '{}-{} год'.format(int(time.strftime("%Y", time.localtime())) - 1,
                                          int(time.strftime("%Y", time.localtime())) + 1 - 1)
    else:
        year_contest = '{}-{} год'.format(int(time.strftime("%Y", time.localtime())),
                                          int(time.strftime("%Y", time.localtime())) + 1)
    return year_contest

