from django.contrib import admin
from .models import Client, Feed_sample, Residue_sample

# Register your models here.
admin.site.register(Client)
admin.site.register(Feed_sample)
admin.site.register(Residue_sample)