from django.contrib import admin

# Register your models here.
from .models import Members,Support,Opinion,Contact

admin.site.register(Members)
admin.site.register(Support)
admin.site.register(Opinion)
admin.site.register(Contact)