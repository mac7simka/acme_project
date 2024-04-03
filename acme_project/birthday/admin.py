from django.contrib import admin


from .models import Birthday


empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'

    )
    list_editable = (
        'birthday',
    )


admin.site.register(Birthday, BirthdayAdmin)
