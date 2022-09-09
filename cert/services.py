from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from cert.models import Cert
from contests.models import Events
from event.models import Event
from contests.models import Archive
from users.models import CustomUser


def get_obj_by_reg_num_from_archive(reg_number, teacher, event):
    user = CustomUser.objects.get(email=str(teacher))
    contest_name = Events.objects.get(id=event).event.name

    try:
        if user.groups.filter(
                name='Manager').exists():
            record = Archive.objects.get(reg_number=reg_number,
                                         contest_name=contest_name)

        else:
            record = Archive.objects.get(reg_number=reg_number,
                                         contest_name=contest_name,
                                         teacher_id=user.id)
        return record
    except ObjectDoesNotExist:
        return None


def get_obj_by_reg_num_from_content_type(reg_number, event_id, teacher):
    event = Events.objects.get(id=event_id)
    model = ContentType.objects.get(app_label=event.app, model=event.model)

    user = CustomUser.objects.get(email=str(teacher))
    try:
        if user.groups.filter(
                name='Manager').exists():
            record = model.get_object_for_this_type(reg_number=reg_number)

        else:
            record = model.get_object_for_this_type(reg_number=reg_number,
                                                    teacher_id=teacher)
        return record
    except ObjectDoesNotExist:
        return None


def get_blank_cert(contest, status, year):
    blank = Cert.objects.get(contest=contest, status=status, year_contest=year)
    return blank
