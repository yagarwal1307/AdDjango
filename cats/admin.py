from django.contrib import admin
from cats.models import Cat, Breed

# Register your models here.
admin.site.register(Breed)
admin.site.register(Cat)