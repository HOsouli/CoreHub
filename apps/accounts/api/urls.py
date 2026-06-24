from django.urls import path
from .views import SendOTP,VerifyOTP, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "accounts"

urlpatterns = [
    path("send-otp/", SendOTP.as_view(), name="send_otp"),
    path("verify-otp/", VerifyOTP.as_view(), name="verify_otp"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

