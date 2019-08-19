from django.urls import include, path
from company.views import CreateTermsView, UpdateTermsView


app_name ='company'
urlpatterns = [
    path('create-terms/', CreateTermsView.as_view(), name='createterms'),
    path('update-terms/<int:pk>/', UpdateTermsView.as_view(), name='updateterms'),

]
