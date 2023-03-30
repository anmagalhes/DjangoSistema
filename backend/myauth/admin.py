from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.register(User, UserAdmin)

# from django.contrib import admin
# from myauth.models import *

# admin.site.register(Pessoa)
# admin.site.register(Gerente)
# admin.site.register(Empresa)
# admin.site.register(Vendedor)
