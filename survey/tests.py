import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from survey.models import Question, Answer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="user", password="pass")


@pytest.fixture
def question(db):
    return Question.objects.create(text="Сколько планет в солнечной системе?")


@pytest.fixture
def answer(db, question):
    return Answer.objects.create(
        question_id=question,
        user_id="550e8400-e29b-41d4-a716-446655440000",
        text="Восемь",
    )


@pytest.mark.django_db
class TestQuestionView:

    def test_get_question_list(self, api_client, question):
        """Проверка корректнось выполнения запроса к списку вопросов"""
        response = api_client.get(reverse("question-list"))
        assert response.status_code == status.HTTP_200_OK

    def test_post_question(self, api_client):
        """Создаем вопрос, проверяем результат"""
        response = api_client.post(
            reverse("question-list"),
            {"text": "Что появилось раньше - курица или яйцо?"},
            format="json",
        )
        assert response.status_code == status.HTTP_201_CREATED

        question_id = response.data["id"]
        response = api_client.get(reverse("question-detail", args=[question_id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["text"] == "Что появилось раньше - курица или яйцо?"

    def test_get_question_retrieve(self, api_client, question):
        """Получение одного вопроса"""
        response = api_client.get(reverse("question-detail", args=[question.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["text"] == "Сколько планет в солнечной системе?"
