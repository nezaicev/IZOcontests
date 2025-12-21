from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from .models import ProfileURAO, Image
from django.utils.html import format_html


def is_manager_or_superuser(user):
    return (
        user.is_superuser
        or user.groups.filter(name='URAO').exists()
    )

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('preview', 'author_name', 'image','size', 'material', 'year')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:80px;"/>',
                obj.image.url
            )
        return '—'


@admin.register(ProfileURAO)
class ProfileURAOAdmin(admin.ModelAdmin):
    search_fields = ('user__email', 'user__fio')
    exclude = ('user',)
    inlines = [ImageInline]

    readonly_fields = ('user_fio', 'user_email')

    fieldsets = (
        ('Пользователь', {
            'fields': ('user_fio', 'user_email'),
        }),
        ('Профиль', {
            'fields': ('bio', 'avatar'),
        }),
    )

    def user_fio(self, obj):
        return obj.user.fio if obj and obj.user else '—'

    user_fio.short_description = 'ФИО'

    def user_email(self, obj):
        return obj.user.email if obj and obj.user else '—'

    user_email.short_description = 'Email'

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if is_manager_or_superuser(request.user):
            return qs  # видят все профили

        return qs.filter(user=request.user)

    def has_add_permission(self, request):
        # профиль создаётся автоматически, пользователь не добавляет
        return False

        # 🔹 Кто может редактировать профиль
    def has_change_permission(self, request, obj=None):
        if is_manager_or_superuser(request.user):
            return True

        if obj is None:
            return True

        return obj.user == request.user

    # Перенаправление на форму профиля вместо списка
    # 🔹 Редирект только для обычных пользователей
    def changelist_view(self, request, extra_context=None):
        if not is_manager_or_superuser(request.user):
            profile = self.get_queryset(request).get(user=request.user)
            return redirect(
                reverse('admin:urao_profileurao_change', args=(profile.pk,))
            )

        # superuser и manager видят список
        return super().changelist_view(request, extra_context)