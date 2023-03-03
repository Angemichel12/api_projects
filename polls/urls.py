from django.urls import path
from .views import poll_list, poll_detail   


urlpatterns = [
    path("polls/", poll_list, name="polls_list"),
    path("polls/<int:pk>/", poll_detail, name="polls_detail"),
   
]
