from django.urls import path
from . import views
# from .views import PostListView, PostDetailView



app_name = 'itreporting'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/',views.about, name= 'about'),
    # path('report/', views.report, name='report'),
    path('report/', views.PostListView.as_view(), name = 'report'),
    path('issues/<int:pk>', views.PostDetailView.as_view(), name = 'issue-detail'),
    path('issue/new', views.PostCreateView.as_view(), name = 'issue-create'),
]