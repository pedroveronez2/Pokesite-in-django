from django.contrib import admin
from .models import Pokemon

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Pokemon)