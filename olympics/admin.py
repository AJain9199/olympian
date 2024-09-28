from django.contrib import admin
from .models import Athlete, Highlight

# Register your models here.


class AtheleteAdmin(admin.ModelAdmin):
    pass

class HighlightAdmin(admin.ModelAdmin):
    pass


admin.site.register(Athlete, AtheleteAdmin)
admin.site.register(Highlight, HighlightAdmin)