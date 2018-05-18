from django.contrib import admin
from .models import Guide, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GuideAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'pnumber', 'group')
    list_filter = ('group',)
    list_select_related = ('group',)


admin.site.register(Guide, GuideAdmin)
admin.site.register(Group, GroupAdmin)