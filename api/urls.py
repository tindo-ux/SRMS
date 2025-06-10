from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, LoginView, UserProfileView,
    SchoolListView, SchoolDetailView,
    ParticipantListView, ParticipantDetailView,
    EventListView, EventDetailView,
    EventParticipantView, EventResultsView,
    NotificationListView, MarkNotificationAsReadView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('schools/', SchoolListView.as_view(), name='school-list'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    
    path('participants/', ParticipantListView.as_view(), name='participant-list'),
    path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant-detail'),
    
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/participants/', EventParticipantView.as_view(), name='event-participant'),
    path('events/<int:pk>/results/', EventResultsView.as_view(), name='event-results'),
    
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/read/', MarkNotificationAsReadView.as_view(), name='notification-read'),
]