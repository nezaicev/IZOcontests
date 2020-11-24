from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, Position, Status, District, Region, Age


class CustomUserAdmin(UserAdmin):
    group_manager='Manager'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'fio')
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'fio', 'region', 'status','school','city','position','phone','Age')}),
        ('Permissions',
         {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    ordering = ('email',)

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(name=self.group_manager).exists():
            return super(CustomUserAdmin, self).get_queryset(request)
        else:
            qs = super(CustomUserAdmin, self).get_queryset(request)
            return qs.filter(email=request.user)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
        # if obj:
        if request.user.is_superuser:
            return fieldsets
        else:
            return ((None, dict(fieldsets)[None]),)

    class Media:
        css = {'all': ('/static/dadata/css/suggestions.min.css',
                       )}
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
            'https://cdn.jsdelivr.net/npm/suggestions-jquery@20.3.0/dist/js/jquery.suggestions.min.js',
            '/static/dadata/js/organizations.js']


class PositionAdmin(admin.ModelAdmin):
    model = Position
    list_display = ['name']


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['name']


class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = ['name']


class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = ['name']


class AgeAdmin(admin.ModelAdmin):
    model = Age
    list_display = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Age, AgeAdmin)
