from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TakenQuiz)
admin.site.register(Profile)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Learner)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Tutorial)
admin.site.register(Notes)
admin.site.register(Announcement)
admin.site.register(LearnerAnswer)
admin.site.register(LessonProgress)

