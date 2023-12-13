from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='blog_home'),
    path('details/<int:id>/',views.DetailsView, name='detail-post'),
    path('delete/<int:id>/',views.DeleteView),
    path('addpost/',views.AddPost),
    path('editpost/<int:id>',views.EditPost),
    path('mypost/<int:id>',views.MyPosts),
    path('like/<int:id>', views.LikeView, name='like'),

]