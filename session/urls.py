from django.urls import include, path
from session.views import (SessionCreateView, SessionListView, LengthError,
                           SessionCategoriesView, SetPriceView, CategorizedSessionListView,
                           SessionUpdateView,SessionDeleteView,SessionCreateView_2,
                           InterferenceErrorView, BoundaryErrorView, NoInputErrorView,
                           LastDataSetView, LogicalErrorView, AllSessionListView,
                           SetDiscountPercentageView, SessionWorkSpaceView,StatusChangeView,
                           IsBookedErrorView,DayListView)

app_name ='session'
urlpatterns = [
    path('sessions-list/', AllSessionListView.as_view(), name='all_sessions_list'),
    path('<int:pk>/create/', SessionCreateView, name='create'),
    path('<int:pk>/list/', SessionListView, name='list'),
    path('<int:pk>/workspace/', SessionWorkSpaceView, name='workspace'),
    path('length-error', LengthError.as_view(), name='lengtherror'),
    path('boundary-error', BoundaryErrorView.as_view(), name='boundaryerror'),
    path('noinput-error', NoInputErrorView.as_view(), name='noinputerror'),
    path('is-booked-error', IsBookedErrorView.as_view(), name='is_booked'),
    path('logical-error', LogicalErrorView.as_view(), name='logicalerror'),
    path('categories/<int:pk>/', SessionCategoriesView, name='categories'),
    path('categorized-sessions/<int:pk>/', CategorizedSessionListView, name='categorizedsessions'),
    path('set-price/<int:pk>/', SetPriceView, name='setprice'),
    path('set-discount-percentage/<int:pk>/', SetDiscountPercentageView, name='setdiscountpercentage'),
    path('status-change/<int:pk>/', StatusChangeView, name='statuschange'),
    path('update/<int:pk>/', SessionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SessionDeleteView, name='delete'),
    path('create2/<int:pk>/', SessionCreateView_2, name='create_2'),
    path('interference-error/<int:pk>/', InterferenceErrorView, name='interferenceerror'),
    path('lastdata-set/<int:pk>/', LastDataSetView, name='lastdataset'),
    path('day-list/<int:pk>/<str:str>/', DayListView, name='day_list'),


]
