from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        # by default django has username, email and password
        fields = ['username', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirmation']
        
        if password != password_confirmation:
            raise serializers.ValidationError({"error" : "Password and Confirmation Password should be the same"})
        
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"error" : "Email is already registered"})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account