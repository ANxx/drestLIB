from rest_framework import serializers

from django.contrib.auth.models import User
from . models import Library
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token



class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True,validators=[UniqueValidator(
                                                    queryset=User.objects.all())])
                                
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField (write_only=True, required=True)
    '''
    Unique Validator varifies amongst all User uniue is TRUE objects in our database.
    Validate whether the password meets all validator requirements.
    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError.
    '''



    class Meta:
        model = User
        fields = ('id','username','email','password','password2','first_name','last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
            }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password did not match"})
        return attrs

    
    def create(self, validated_data):
        '''
           return complete object instances based on the validated data
        '''
        user = User.objects.create(email=validated_data['email'],username=validated_data['username'],
                        first_name=validated_data['first_name'],last_name=validated_data['last_name'],)
        
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id','title','catagory','published_date')



