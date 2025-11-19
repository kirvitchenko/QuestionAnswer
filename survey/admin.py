from django.contrib import admin

from survey.models import Answer, Question

admin.site.register(Question)
admin.site.register(Answer)
