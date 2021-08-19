from contests.models import ModxDbimgMuz, ShowEvent, CustomUser, PageContest


def exists_record_vm(oldname):
    ModxDbimgMuz.objects.using('vm').get(oldname=oldname)


def subscribe_show_event(teacher, page_contest):
    result=ShowEvent.objects.create(
        teacher=CustomUser.objects.get(id=teacher),
        page_contest=PageContest.objects.get(id=page_contest))
    return result


def get_show_evens_by_user(user):
    if user.is_authenticated:
        user_show_evens_tuple = ShowEvent.objects.filter(
            teacher_id=user.id).values_list('page_contest')
        if user_show_evens_tuple:
            return user_show_evens_tuple[0]
    else:
        return None
