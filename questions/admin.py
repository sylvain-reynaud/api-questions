from django.contrib import admin

from .models import Question, Theme

admin.site.register(Question)
admin.site.register(Theme)