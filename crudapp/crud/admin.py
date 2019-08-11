from django.contrib import admin
from .models import Programming


class ProgrammingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('language', )} # =====> in order to make the language equal to slug automatically 


admin.site.register(Programming, ProgrammingAdmin)