from django.urls import path

#-------- User Request view Import --------#
from .views import FoodRequest,Service_Amenities_Request,Washing_machine_Request_View
from user_request import views as request_show_view
from user_request.views import WashingDetailView,WashingDeleteView,WashingUpdateView

urlpatterns = [

    path('food_request/',FoodRequest.as_view(),name='food-request'),
    path('service_AND_amenities/',Service_Amenities_Request.as_view(),name='service_amenities_request'),
    path('request_show/', request_show_view.show_request,name='service_request_list'),
    path('food_request_show/', request_show_view.show_food_request,name='food_request-show'),
    path('washing_request/',Washing_machine_Request_View.as_view(),name='washing_request'),
    path('washing_request_show/', request_show_view.show_washing_request,name='washing_request_show'),
    path('washing_request_manage/<int:pk>/', WashingDetailView.as_view(), name='washing-detail'),
    path('washing_request_manage/<int:pk>/update/', WashingUpdateView.as_view(), name='washing-update'),
    path('washing_request_manage/<int:pk>/delete/', WashingDeleteView.as_view(), name='washing-delete'),

]