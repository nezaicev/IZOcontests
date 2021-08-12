from django.contrib import admin
from contests.models import Events
from cert.models import Cert, Text, Font

# Register your models here.


admin.site.register(Cert)
admin.site.register(Font)
admin.site.register(Text)