from rest_framework import serializers

from survey.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Серилизатор для ответов с валидацией поля 'text' """
    text = serializers.CharField(min_length=1, max_length=2000)

    class Meta:
        model = Answer
        fields = ["id", "text", "created_at",  "user_id"]
        read_only_fields = ["created_at", "id",  "user_id"]


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов с валидацией поля 'text' и вложенным сериализатором для ответов"""
    answers = AnswerSerializer(many=True, read_only=True)
    text = serializers.CharField(min_length=10, max_length=1000)

    class Meta:
        model = Question
        fields = ["id", "text", "created_at", "answers"]
        read_only_fields = ["created_at", "id", "answers"]
