from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from .models import Question, Quiz


class QuizView(ListView):

    def get(self, request):
        quiz_objs = Quiz.objects.all()
        return render(request, 'quiz.html', {'quiz_objs': quiz_objs})

    def post(self, request):
        post_data = request.POST.dict()
        if 'modify_val' in post_data:
            modify_id = request.POST.getlist('quiz_id')
            modify_name = request.POST.getlist('quiz_name')
            modify_data = dict(zip(modify_id, modify_name))
            for id, new_name in modify_data.items():
                quiz_obj = Quiz.objects.filter(quiz_id=id)
                if quiz_obj.first().name != new_name:
                    quiz_obj.update(name=new_name)
                    messages.success(request, 'Quiz has been updated.')
            return self.get(request)
        new_data = request.POST.dict()
        quiz = new_data['quiz_name']
        description = new_data['quiz_des']
        if quiz is '' and description is '':
            messages.warning(request, 'Please enter some text')
            return self.get(request)
        Quiz.objects.create(name=quiz, description=description)
        messages.success(request, 'Quiz has been Inserted.')
        return self.get(request)


class QuestionView(ListView):

    def get(self, request):
        ques_objs = Question.objects.all()
        return render(request, 'question.html', {'ques_objs': ques_objs})

    def post(self, request):
        data = request.POST.dict()
        if 'question_text' not in data:
            messages.warning(request, 'Please Select a Question')
            ques_objs = Question.objects.all()
            return render(request, 'question.html', {'ques_objs': ques_objs})
        elif len(request.POST.getlist('question_text')) > 1:
            messages.warning(request, 'Please Select Only one Question')
            ques_objs = Question.objects.all()
            return render(request, 'question.html', {'ques_objs': ques_objs})
        else:
            question = data['question_text']
            return render_to_response('answer_form.html',
                                      {'question': question})
