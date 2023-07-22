# artists/urls.py
from django.urls import path
from .views import WorkListCreateView, ArtistListCreateView, ArtistDetailView

urlpatterns = [
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
]
