from rest_framework.routers import SimpleRouter

from survey.views import AnswersView, QuestionView

router = SimpleRouter()
router.register("question", QuestionView, basename="question")
router.register("answers", AnswersView, basename="answers")

urlpatterns = [*router.urls]
