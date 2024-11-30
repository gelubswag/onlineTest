from django.contrib import admin
from testApp import models

admin.site.register(models.Subject)
admin.site.register(models.SubjTest)
admin.site.register(models.Question)
admin.site.register(models.UserTest)
admin.site.register(models.UserAnswer)
admin.site.register(models.Option)

# Register your models here.
