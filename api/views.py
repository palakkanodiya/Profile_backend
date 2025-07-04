from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import ProfileModel
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django backend!"})

class Profile(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    


from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Django backend is running ✅"})
