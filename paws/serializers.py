from rest_framework import serializers

from .models import Food, Question, Answer, User

class FoodsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'dog_owned')
        depth = 2

class QRUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class AnswerSerializer(serializers.ModelSerializer):
    response_by = QRUserSerializer
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    asked_by = QRUserSerializer
    answers = AnswerSerializer
    class Meta:
        model = Question
        fields = '__all__'
        depth = 2