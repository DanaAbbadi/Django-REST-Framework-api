from django.urls import path, include
from .views import FriendsList, FriendsDetails

urlpatterns = [
    path('', FriendsList.as_view(), name='friends'), 
    path('<int:pk>/', FriendsDetails.as_view(), name='friends_details')  
]