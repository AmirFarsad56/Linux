from django.urls import include, path
from accounts.views import (SuperUserProfileView, SuperUserUpdateView,
                            CloudMessageView, CloudEmailView, PasswordChangeView,
                            SuperUserWorkSpaceView)

app_name ='accounts'
urlpatterns = [
    path('profile/<slug:slug>/', SuperUserProfileView, name='profile'),
    path('workspace/<slug:slug>/', SuperUserWorkSpaceView, name='workspace'),
    path('update/<slug:slug>/', SuperUserUpdateView, name='update'),
    path('cloudmessage/', CloudMessageView, name='cloudmessage'),
    path('cloudemail/', CloudEmailView, name='cloudemail'),
    path('passwordchange/<slug:slug>/', PasswordChangeView, name='passwordchange'),
]
