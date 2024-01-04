# main/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Question, Posts, Topic, Users, Employement, Education, Location,Vote, Answer, Comment
from .serializers import QuestionSerializer, PostsSerializer, TopicSerializer, UsersSerializer, EmployementSerializer, EducationSerializer, LocationSerializer,VoteSerializer, AnswerSerializer, CommentSerializer


def home(request):
    return JsonResponse({'Info':'React & Django', "name":"1NURSE"})
class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class PostsCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostsList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicCreateView(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class UsersCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class EmployementCreateView(generics.CreateAPIView):
    queryset = Employement.objects.all()
    serializer_class = EmployementSerializer

class EmployementList(generics.ListAPIView):
    queryset = Employement.objects.all()
    serializer_class = EmployementSerializer

class EducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationList(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteList(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class NotificationsList(generics.ListAPIView):
#     queryset = Notifications.objects.all()
#     serializer_class = NotificationsSerializer

# class NotificationsList(generics.CreateAPIView):  
#     queryset = Notifications.objects.all()
#     serializer_class = NotificationsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)