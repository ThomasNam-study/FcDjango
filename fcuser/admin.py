from django.contrib import admin

# Register your models here.
from fcuser.models import Fcuser


class FcUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Fcuser, FcUserAdmin)