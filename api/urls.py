from django.urls import path
from .views import HelloWorldView , Profile, ProfileDetail

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('profiles/', Profile.as_view()),
    path('ProfileDetail/', ProfileDetail.as_view(),name='ProfileDetail'),
    path('profiledeatil/<int:pk>/', ProfileDetail.as_view())
]

