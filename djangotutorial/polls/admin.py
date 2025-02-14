from django.contrib import admin

from .models import Question, Virtuals, User, Choice


admin.site.register(Question)
admin.site.register(Virtuals)
admin.site.register(Choice)

# Register your models here.
