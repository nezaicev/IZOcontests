from django.urls import path
from cert.views import ConfirmationUserDataView, SearchRegNumView, ConfirmationParticipantCertEvent

urlpatterns = [
    path('', SearchRegNumView.as_view(), name='search_cert'),
    path('confirmation/', ConfirmationUserDataView.as_view(), name='confirmation_data_view'),
    path('confirmation/event/', ConfirmationParticipantCertEvent.as_view(), name='confirmation_data_cert_for_event')
]