from django.urls import include, path
from booking.views import (CreateProfitPercentageView, UpdateProfitPercentageView,
                            BookingView)


app_name ='booking'
urlpatterns = [
    path('create-profit-percentage/', CreateProfitPercentageView.as_view(), name='createprofitpercentage'),
    path('update-profit-percentage/<int:pk>/', UpdateProfitPercentageView.as_view(), name='updateprofitpercentage'),
    path('booking/<int:pk>/', BookingView, name='booking'),


]
