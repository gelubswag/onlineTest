from django.contrib import admin
from testApp import models
admin.site.register(models.Subject)
admin.site.register(models.SubjTest)
admin.site.register(models.Question)

# Register your models here.
