from django.urls import include, path
from session.views import (SessionCreateView, SessionListView, LengthError,
                           SessionCategoriesView, SetPriceView, CategorizedSessionListView,
                           SessionUpdateView,SessionDeleteView)

app_name ='session'
urlpatterns = [
    path('create/<int:pk>/', SessionCreateView, name='create'),
    path('list/<int:pk>/', SessionListView, name='list'),
    path('length-error', LengthError.as_view(), name='lengtherror'),
    path('categories/<int:pk>/', SessionCategoriesView, name='categories'),
    path('categorizedsessions/<int:pk>/', CategorizedSessionListView, name='categorizedsessions'),
    path('setprice/<int:pk>/', SetPriceView, name='setprice'),
    path('update/<int:pk>/', SessionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SessionDeleteView, name='delete'),


]