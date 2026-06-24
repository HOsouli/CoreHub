from rest_framework.views import APIView
from rest_framework.response import Response  # To return standard API output
from rest_framework import status
from apps.accounts.services.otp_service import create_otp, verify_otp
from apps.accounts.api.serializers import SendOTPSerializer, VerifyOTPSeializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.accounts.api.serializers import ProfileSerializer
from apps.accounts.services.tasks import send_otp_sms_task


class SendOTP(APIView):
    permission_classes = [AllowAny]
    serializer_class = SendOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data["phone_number"]

        create_otp(phone_number)

        return Response(
            {"message": "OTP sent successfully", "phone_number": phone_number},
            status=status.HTTP_201_CREATED,
        )

# _____________________________________________________________________________
class VerifyOTP(APIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyOTPSeializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data["phone_number"]
        code = serializer.validated_data["code"]
        result = verify_otp(phone_number=phone_number, code=code)

        return Response(
            {
                "message": "OTP verified successfully",
                "is_new_user": result["created"],
                "tokens": result["tokens"],
            },
            status=status.HTTP_200_OK,
        )


# _____________________________________________________________________________
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)  # Get current user information
        return Response(serializer.data)

    def patch(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# _____________________________________________________________________________
