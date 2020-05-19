from django.shortcuts import render
from rest_framework import generics
from . models import MyUser,ForumCommentsImages,ForumsComments,ForumsPostImage,ForumsPost
#from . serilizers import MyUserSerilizer,ForumsPostSerializer,ForumsCommentSerializer,ForumsPostImageSerializer,ForumCommentsImages
from . serilizers import UserSerilizer,PostSerializer,PostImageSerializer,CommentSerializer,CommentsImagesSerializer
# Create your views here.
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=MyUser.objects.all()
    serializer_class=UserSerilizer
class UserDetailsList(generics.ListCreateAPIView):
    queryset=MyUser.objects.all()
    serializer_class=UserSerilizer
#Forumpost
class ForumsPostDetails(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=ForumsPost.objects.all()
    serializer_class= PostSerializer
class ForumsPostDetailsList(generics.ListCreateAPIView):
    queryset=ForumsPost.objects.all()
    serializer_class= PostSerializer
#post image
class ForumsPostImageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ForumsPostImage.objects.all()
    serializer_class=PostImageSerializer
class ForumsPostImageList(generics.ListAPIView):
    queryset=ForumsPostImage.objects.all()
    serializer_class=PostImageSerializer
#forum comment
class ForumsCommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ForumsComments.objects.all()
    serializer_class=CommentSerializer
class ForumsCommentsList(generics.ListAPIView):
    queryset=ForumsComments.objects.all()
    serializer_class=CommentSerializer
#forum comment image
class ForumCommentsImagesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ForumCommentsImages.objects.all()
    serializer_class=CommentsImagesSerializer
#comment image
class ForumCommentsImagesList(generics.ListCreateAPIView):
    queryset=ForumCommentsImages.objects.all()
    serializer_class=CommentsImagesSerializer



    