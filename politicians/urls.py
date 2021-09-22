from django.urls import path
from .views import PostListView, AddCommentView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='politician-list'),
    # path('politician/<int:pk>/', PostDetailView.as_view(), name='politician-detail'),
    path('politician/<int:id>/', views.post_detail_view, name ='politician-detail'),
    path('about/', views.about, name='politician-about'),
    path('search/', views.search_venues, name='search-venues'),
    path('review/', views.Review_rate, name='review'),
    path('contact/', views.contact, name='politician-contact'),
    path('politician/<int:pk>/add-review/', AddCommentView.as_view(), name="add_comment")
]