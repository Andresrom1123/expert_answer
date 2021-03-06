from django.urls import path, include
from rest_framework import routers

from answers.views import AnswerViewSet
from comments.views import CommentViewSet
from interests.views import InterestViewSet
from questions.views import QuestionViewSet
from topics.views import TopicViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'interests', InterestViewSet)

urlpatterns = [
    path('', include(router.urls))
]