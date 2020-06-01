from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # To show the readonly field 'created' in admin page
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
