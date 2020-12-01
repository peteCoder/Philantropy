from django.urls import path
from . import views

urlpatterns = [
	#path('', views.blog, name="blog"),
	path('', views.Blog.as_view(), name="blog"),
	
	path('<int:pk>/', views.blog_single, name="article_detail"),
	path('add_post/', views.AddPostView.as_view(), name='add_post'),
	path('update_post/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
	path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
	
	
	path('like/<int:pk>', views.LikeView, name="like_post"),
	
]