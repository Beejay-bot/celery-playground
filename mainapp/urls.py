from django.urls import path
from .views import test, send_mail_to_all

urlpatterns = [
    path('',test, name='test_view' ),
    path('sendmail/',send_mail_to_all, name='send mail' ),
]

