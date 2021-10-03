from django.contrib import admin

from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fields = ('id',
              'email',
              'password',
              'first_name',
              'last_name',
              'phone',
              'birthday',
              'gender',
              'bio',
              'ethnicity',
              'country',
              'city',
              'region')

    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',
                    'phone',
                    'birthday',
                    'gender',
                    'ethnicity',
                    'country',
                    'city',
                    'region')

    list_filter = ('first_name',
                   'last_name',
                   'phone',
                   'birthday',
                   'gender',
                   'ethnicity',
                   'country',
                   'city')

    ordering = ('last_name',)
    readonly_fields = ('id',)
