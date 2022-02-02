from django.contrib import admin

from .models import Dog, Food, Question, Task, User, Answer
# Register your models here.

admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Food)
admin.site.register(Question)
admin.site.register(Dog)
admin.site.register(Task)
