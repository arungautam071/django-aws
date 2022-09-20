#--------Django Import--------#
from django.urls import path

#-------- Services Management View Import--------#
from .views import pharamacy_request_ListView,pharmacy_requestUpdateView,pharmacy_requestDeleteView
from .views import pharmacy_requestCreateView,detail_view_pharmacy

#-------- URL Pattern--------#
urlpatterns = [
    path('pharmacy/request/', pharmacy_requestCreateView.as_view(), name='request_pharmacy-create'),
    path('pharamacy_request_List/',pharamacy_request_ListView.as_view(),name='pharamacy_request-list'),
    path('pharmacy_request_Form/<int:pk>/update/',pharmacy_requestUpdateView.as_view(),name='user_status_update'),
    path('entry_delete/<int:pk>/delete/', pharmacy_requestDeleteView.as_view(), name='request-delete'),
    path('<id>/', detail_view_pharmacy,name='request-detail'),
]