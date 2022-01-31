from django.contrib import admin

from .models import Dog, Food, Question, User, Response
# Register your models here.

admin.site.register(User)
admin.site.register(Response)
admin.site.register(Food)
admin.site.register(Question)
admin.site.register(Dog)
