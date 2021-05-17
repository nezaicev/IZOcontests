from django.urls import path
from cert.views import SearchRegNumView,ConfirmationUserDataView

urlpatterns = [
    path('', SearchRegNumView.as_view(), name='search_cert'),
    path('confirmation/', ConfirmationUserDataView.as_view(), name='confirmation_data_view')
]