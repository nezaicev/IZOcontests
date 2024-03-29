# Generated by Django 3.2 on 2023-06-07 09:41
import csv
from django.db import migrations



def update(apps, schema_editor):
    data = []
    Archive = apps.get_model('contests', 'Archive')
    with open('./2021_artakiada.csv', newline='') as file:
        rows = csv.reader(file, delimiter=',', )
        for i in rows:
            data.append(i)
    for i in data:
        print(i[0])
        obj = Archive.objects.filter(reg_number=i[0])

        if obj:
            print(obj)
            obj[0].level=i[5]
            obj[0].material = i[3]
            obj[0].author_name = i[2]
            obj[0].publish = True
            obj[0].save()


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0144_auto_20230526_1509'),
    ]

    operations = [
        migrations.RunPython(update)
    ]
