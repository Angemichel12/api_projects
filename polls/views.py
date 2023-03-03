from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.decorators import api_view
from .models import Poll
from .serializers import PollSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser





@api_view(['GET', 'POST'])
def poll_list(request):
    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True).data
        return Response(serializer)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == 'GET':
        serializer = PollSerializer(poll).data
        return Response(serializer)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PollSerializer(poll, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        poll.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
