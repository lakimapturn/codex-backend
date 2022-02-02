from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('foods', views.FoodsAPI.as_view(), name="foodsAPI"),
    path('auth', views.CustomAuthToken.as_view(), name="authAPI"),
    path('question-response', views.QuestionAPI.as_view(), name="q&aAPI"),
    path('answer', views.AnswerAPI.as_view(), name="answerAPI")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)