from django.contrib import admin
from core.models import User


class User_Admin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'username',
    )
    readonly_fields = ('last_login', 'date_joined')
    exclude = ('password',)

admin.site.register(User, User_Admin)