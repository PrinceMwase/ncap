from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class CLinicNurseListFilter(admin.SimpleListFilter):
    title = _('nurse')

    parameter_name = 'nurse'
    
    def lookups(self, request, model_admin):
        
        if request.user.groups.filter(name='nurse') : 
            return (
                ('all', _('all nurses')),
                ('mine', _('by me'))
            )
        
    def queryset(self, request, queryset):
        if self.value() == 'mine':
            return queryset.filter(
                nurse=request.user.actor.nurse.id
            )

        
    
