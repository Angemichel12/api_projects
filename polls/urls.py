from django.urls import path
from .views import PollList, PollDetail,UserLIst,UserDetail  


urlpatterns = [
    path("polls/", PollList.as_view()),
    path("polls/<int:pk>/", PollDetail.as_view()),
    path("users/", UserLIst.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
]


