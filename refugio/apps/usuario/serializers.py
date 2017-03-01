from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):

	class Meta:
		model = User#El modelo es User
		fields = ('first_name', 'email')#Los campos son first_name y email
