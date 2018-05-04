import uuid
from django.db import models

# Create your models here.


class Quiz(models.Model):
    """
    Quiz's model, works as a wrapper for the questions
    """
    quiz_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=220, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=120, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, related_name='questions')

    def __str__(self):
        return "{content} - {published}".format(
            content=self.question_text, published=self.is_published)


class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    text = models.CharField(max_length=120, null=True, blank=True)
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers')

    def __str__(self):
        return self.text
