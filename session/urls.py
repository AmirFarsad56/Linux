from django.urls import include, path
from session.views import (SessionCreateView, SessionListView, LengthError,
                           SessionCategoriesView, SetPriceView, CategorizedSessionListView,
                           SessionUpdateView,SessionDeleteView,SessionCreateView_2,
                           InterferenceErrorView, BoundaryErrorView, NoInputErrorView,
                           LastDataSetView, LogicalErrorView, AllSessionListView)

app_name ='session'
urlpatterns = [
    path('sessions-list/', AllSessionListView.as_view(), name='all_sessions_list'),
    path('create/<int:pk>/', SessionCreateView, name='create'),
    path('list/<int:pk>/', SessionListView, name='list'),
    path('length-error', LengthError.as_view(), name='lengtherror'),
    path('boundary-error', BoundaryErrorView.as_view(), name='boundaryerror'),
    path('noinput-error', NoInputErrorView.as_view(), name='noinputerror'),
    path('logical-error', LogicalErrorView.as_view(), name='logicalerror'),
    path('categories/<int:pk>/', SessionCategoriesView, name='categories'),
    path('categorizedsessions/<int:pk>/', CategorizedSessionListView, name='categorizedsessions'),
    path('setprice/<int:pk>/', SetPriceView, name='setprice'),
    path('update/<int:pk>/', SessionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SessionDeleteView, name='delete'),
    path('create2/<int:pk>/', SessionCreateView_2, name='create_2'),
    path('interference-error/<int:pk>/', InterferenceErrorView, name='interferenceerror'),
    path('lastdataset/<int:pk>/', LastDataSetView, name='lastdataset'),


]
