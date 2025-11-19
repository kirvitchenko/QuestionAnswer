import uuid
from django.db import models


class Question(models.Model):
    """Модель вопроса, содержит в себе текст вопроса и дату создания"""

    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    """Модель ответа, содержит внешний ключ на вопрос, индентификатор пользователя, содержание ответа и дату создания"""

    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user_id = models.CharField(max_length=36, default=uuid.uuid4)
    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
