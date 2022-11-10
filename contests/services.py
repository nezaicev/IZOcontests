from contests.models import ModxDbimgMuz, ShowEvent, CustomUser, PageContest


def exists_record_vm(oldname):
    ModxDbimgMuz.objects.using('vm').get(oldname=oldname)

# def update_phone_number_for_user(user, new_phone):
#     if new_phone:
#         if user.phone!=new_phone:
#             user.phone


def subscribe_show_event(teacher, page_contest):
    result=ShowEvent.objects.create(
        teacher=CustomUser.objects.get(id=teacher),
        page_contest=PageContest.objects.get(id=page_contest))
    return result


def get_show_evens_by_user(user):
    if user.is_authenticated:
        user_show_evens_tuple = ShowEvent.objects.filter(
            teacher_id=user.id).values_list('page_contest')
        user_show_evens_tuple=[id[0] for id in user_show_evens_tuple]
        if user_show_evens_tuple:
            return user_show_evens_tuple
    else:
        return None
