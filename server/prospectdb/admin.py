from django.contrib import admin

from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fields = ('id',
              'email',
              'first_name',
              'last_name',
              'phone',
              'birthday',
              'story',
              'occupation',
              'gender',
              'ethnicity',
              'country',
              'city',
              'region',
              'registered_at',
              'created_at')

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
