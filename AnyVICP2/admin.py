from django.contrib import admin
from .models import *

admin.site.register(Website)
admin.site.register(Announcement)

# For admin management