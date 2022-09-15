from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):
        if not request.session.exists(request.session.session_key):
            request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        host = request.session.session_key
        room, created = Room.objects.get_or_create(host=host)
        room.guest_can_pause = serializer.validated_data['guest_can_pause']
        room.votes_to_skip = serializer.validated_data['votes_to_skip']
        room.save()
        
        status_code = status.HTTP_200_OK if not created else status.HTTP_201_CREATED
        return Response(data=RoomSerializer(room).data, status=status_code)
            
            
            
        
            
            