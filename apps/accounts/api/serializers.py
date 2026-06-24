from rest_framework import serializers
from apps.accounts.models import CustomUser

class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, min_length=11)



class VerifyOTPSeializers(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "email", "first_name", "last_name"]
        read_only_fields = ("phone_number",)


