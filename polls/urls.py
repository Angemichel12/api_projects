from django.urls import path
from .views import PollList, PollDetail,ChoiceList,CreateVote, PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')



urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/",ChoiceList.as_view(), name='choices_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
]
