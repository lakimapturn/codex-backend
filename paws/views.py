from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.views.decorators.csrf import csrf_exempt

from paws.serializers import FoodsSerializer, QuestionSerializer, UserSerializer

from .models import Dog, Food, Question, Task, User, Answer

# Create your views here.

class CustomAuthToken(ObtainAuthToken):    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(User.objects.get(id = user.pk))
        return Response({
			'token': token.key,
			'user': serializer.data
        })

class RegistrationAPI(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        firstName = request.data["first_name"]
        lastName = request.data["last_name"]
        password = request.data["password"]
        email = request.data["email"]

        dog_name = request.data["dog_name"]
        dog_breed = request.data["dog_breed"]
        dog_age = request.data["dog_age"]
        dog_picture = request.data["dog_image"]
        dog_vaccinated = request.data["dog_vaccinated"]
        dog_microchipped = request.data["dog_vaccinated"]

        dog = Dog.objects.create(
            name = dog_name, 
            age = dog_age, 
            breed = dog_breed, 
            picture = dog_picture, 
            vaccinated = dog_vaccinated, 
            microchipped = dog_microchipped
        )

        try: 
            user = User.objects.create_user(username = username, email = email, password = password, first_name = firstName, last_name = lastName, dog_owned = dog)
            user.save()
        except IntegrityError as err:
            print(err)
            return Response("Username Already Exists!", status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(user, status=status.HTTP_201_CREATED)

class DogAPI(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        dog = Dog.objects.get(id = request.data['dog'].id)
        dog = request.data['dog']
        dog.save()

        return Response(status=status.HTTP_202_ACCEPTED)


class UsersAPI(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        pass

    @csrf_exempt 
    def post(self, request, *args, **kwargs):
        if request.method == 'POST': # If the user is attempting to login this function runs
            enteredUsername = request.POST["username"]
            enteredPassword = request.POST["password"]
            user = authenticate(request, username = enteredUsername, password = enteredPassword)

            if user is not None: # checking if the user exists or not
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

class FoodsAPI(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            queryset = Food.objects.all()
            serializer = FoodsSerializer(queryset, many=True)

            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class QuestionAPI(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            queryset = Question.objects.all()
            serializer = QuestionSerializer(queryset, many=True)

            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id = request.data['user'])
            question = Question.objects.create(question = request.data['question'], asked_by = user)
            question.save()
            queryset = Question.objects.all()
            serializer = QuestionSerializer(queryset, many=True)

            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnswerAPI(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id = request.data['user'])
            question = Question.objects.get(id = request.data['question'])
            answer = Answer.objects.create(response = request.data['answer'], response_by = user)
            answer.save()
            question.answers.add(answer)
            question.save()
            queryset = Question.objects.all()
            serializer = QuestionSerializer(queryset, many=True)

            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def index(request):
    return HttpResponse("Hello!")