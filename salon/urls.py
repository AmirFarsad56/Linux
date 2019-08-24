from django.urls import include, path
from salon.views import (SalonCreateView, SalonUpdateView, SalonDetailView,
                        ConfirmedSalonListView, UnConfirmedSalonListView,
                        SalonConfirmView, SalonDeleteView, SalonBanView,
                        SalonDetailViewMasterUser,SalonSetProfitPercentage,
                        SalonConfirmView_2,SalonBanView_2,ConfirmModalView,
                        ConfirmModalView_2,BanModalView_2,BanModalView)


app_name ='salon'
urlpatterns = [
    path('profile/<slug:slug>/createsalon/', SalonCreateView, name='createsalon'),
    path('confirmedsalonlist/',ConfirmedSalonListView.as_view(),
        name='confirmedsalonlist'),
    path('unconfirmedsalonlist/',UnConfirmedSalonListView.as_view(),
        name='unconfirmedsalonlist'),
    path('sportclub/<slug:slug>/profile/updatesalon/<int:pk>/',SalonUpdateView, name='update'),
    path('sportclub/profile/salondetail/<int:pk>/',SalonDetailView.as_view(), name='salondetail'),
    path('salon/confirm/<int:pk>/',SalonConfirmView, name='confirm'),
    path('salon/confirm-2/<int:pk>/',SalonConfirmView_2, name='confirm_2'),
    path('salon/confirm-modal/<int:pk>/',ConfirmModalView, name='confirmmodal'),
    path('salon/confirm-modal-2/<int:pk>/',ConfirmModalView_2, name='confirmmodal_2'),
    path('salon/delete/<int:pk>/',SalonDeleteView, name='delete'),
    path('salon/ban/<int:pk>/',SalonBanView, name='ban'),
    path('salon/ban-2/<int:pk>/',SalonBanView_2, name='ban_2'),
    path('salon/ban-modal/<int:pk>/',BanModalView, name='banmodal'),
    path('salon/ban-modal-2/<int:pk>/',BanModalView_2, name='banmodal_2'),
    path('salon/detail/<int:pk>/',SalonDetailViewMasterUser, name='detail'),
    path('salon/setprofitpercentage/<int:pk>/',SalonSetProfitPercentage, name='setprofitpercentage'),

]
