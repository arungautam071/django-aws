#-------- Django Default Impor--------#
from django.urls import path

#-------- Room Management View Import--------#

from .views import Room_Management_View, Room_ManagementListView
from room_management.views import RoomUpdateView,RoomEntryDeleteView,detail_view,Add_User_Room_Management_View,User_RoomUpdateView,RoomEntryDeleteView


#-------- URL Pattern--------#S

urlpatterns = [
    #-------- Room management URL --------#
    path('availability/',Room_Management_View.as_view(),name='room-availability'),
    path('room_availability/',Room_ManagementListView.as_view(),name='room-list'),
    path('<int:pk>/update_room',RoomUpdateView.as_view(),name='room-update'),
    path('<int:pk>/delete/', RoomEntryDeleteView.as_view(), name='room-delete'),
    path('add_user/',Add_User_Room_Management_View.as_view(),name='add_user_room'),
    path('user_room_update/<int:pk>/update/', User_RoomUpdateView.as_view(), name='user-room-update'),
    path('entry_delete/<int:pk>/delete/', RoomEntryDeleteView.as_view(), name='entry-delete'),
    path('<id>/detail', detail_view,name='room-detail'),
    
    
]


# path('room_detail/',User_Room_ManagementListView.as_view(),name='user-room-list'),


