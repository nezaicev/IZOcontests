from contests.models import ModxDbimgMuz


def exists_record_vm(oldname):
    ModxDbimgMuz.objects.using('vm').get(oldname=oldname)




