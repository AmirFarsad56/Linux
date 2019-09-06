from django.urls import include, path
from company.views import (CreateTermsView, UpdateTermsView, AccountingDetailView, ReckoninglistView,
                            SalonAdvertisementCreateView, SalonAdvertisementListView,
                            SalonAdvertisementDeleteView)


app_name ='company'
urlpatterns = [
    path('create-terms/', CreateTermsView.as_view(), name='createterms'),
    path('accounting-detail/', AccountingDetailView, name='accountingdetail'),
    path('reckoning-list/', ReckoninglistView, name='reckoninglist'),
    path('update-terms/<int:pk>/', UpdateTermsView.as_view(), name='updateterms'),
    path('salon-advertisement-add/<int:pk>/', SalonAdvertisementCreateView, name='salonadvertisementcreate'),
    path('salon-advertisement-list/', SalonAdvertisementListView.as_view(), name='salonadvertisementlist'),
    path('salon-advertisement-delete/<int:pk>/', SalonAdvertisementDeleteView, name='salonadvertisementdelete'),

]
