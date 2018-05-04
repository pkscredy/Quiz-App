from django.conf.urls import url
from quiz.views import QuestionView, QuizView

app_name = 'quiz'

urlpatterns = [
    url(r'^quiz_detail/$', QuizView.as_view(), name='quiz_detail'),
    url(r'^question/$', QuestionView.as_view(), name='question_detail'),
]
