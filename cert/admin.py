from django.contrib import admin
from cert.models import Events, Cert, Text, Font

# Register your models here.

admin.site.register(Events)
admin.site.register(Cert)
admin.site.register(Font)
admin.site.register(Text)