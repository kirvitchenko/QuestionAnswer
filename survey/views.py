import uuid

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet, ModelViewSet

from survey.models import Question, Answer
from survey.serializers import QuestionSerializer, AnswerSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ["get", "post", "delete"]


    @action(detail=True, methods=["post"], url_path="answers")
    def add_answer(self, request, pk=None):
        """Дополнительный метод с созданием ответов для вопросов по question_id"""
        question = self.get_object()
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_uuid = str(uuid.uuid4())
        serializer.save(question_id=question, user_id=user_uuid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswersView(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    http_method_names = ["get", "delete"]
