from django.contrib import admin
from .models import Athlete

# Register your models here.


class AtheleteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Athlete, AtheleteAdmin)