from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from dropbox_mini.models import Boxofdrop

# Register your models here.

admin.site.register(Boxofdrop, DraggableMPTTAdmin)