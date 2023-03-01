from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Poll, Choice, Vote
from .serializers import PollSerializer,ChoiceSerializer,VoteSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PollViewSet(viewsets.ModelViewSet):
    polls = Poll.objects.all()
    serializer_class = PollSerializer

@api_view(['GET', 'POST'])
def poll_list(request):
    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response({'polls':serializer.data})
    if request.method == 'POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
   
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer
class CreateVote(APIView):
    serializer_class = VoteSerializer
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll':pk, 'voted_by':voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_2O1_CREATED)
        else:
            return  Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)