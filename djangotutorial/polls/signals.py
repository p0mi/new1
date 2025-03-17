from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Question, Choice

@receiver(post_save, sender=Question)
def log_question_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Новый вопрос создан: {instance.question_text}")

@receiver(post_save, sender=Choice)
def log_choice_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Новый выбор создан для вопроса '{instance.question}': {instance.choice_text}")