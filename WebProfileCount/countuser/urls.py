from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
#for future testing check trailing_slash=Flase
router=DefaultRouter()

urlpatterns=[
    path('users/',views.UserDetailsList.as_view(),name='User Details list'),
    path('users/<int:pk>/',views.UserDetails.as_view(),name='User Details'),
   
    path('Forumpost/',views.ForumsPostDetailsList.as_view(),name='Post List'),
    path('Forumpost/<int:pk>/',views.ForumsPostDetails.as_view(),name="Post details"),
    path('ForumpostImage/<int:pk>/',views.ForumsPostImageDetails.as_view(),name="Image Details"),
    path('ForumpostImage/',views.ForumsPostImageList.as_view(),name='Post Image List'),
    path('Forumcomment/<int:pk>/',views.ForumsCommentsDetails.as_view(),name="Comment Details"),
    path('Forumcomment/',views.ForumsCommentsList.as_view(),name="Comment List"),
    path('ForumcommentImage/<int:pk>/',views.ForumCommentsImagesDetails.as_view(),name="Comment Image Details"),
    path('ForumcommentImage/',views.ForumCommentsImagesList.as_view(),name="Comment Image List"),


]

