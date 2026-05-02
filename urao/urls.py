from django.urls import path

from .views import SignUpView, ProfileURAOListView, ProfileURAODetailView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_urao'),
    path('api/profiles/', ProfileURAOListView.as_view(), name='urao_profiles_list'),
    path('api/profiles/<int:pk>/', ProfileURAODetailView.as_view(), name='urao_profile_detail'),
]