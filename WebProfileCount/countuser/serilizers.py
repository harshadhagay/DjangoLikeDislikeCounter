from rest_framework import serializers
from .models import ForumCommentsImages,ForumsComments,ForumsPost,ForumsPostImage,MyUser
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=('user','username','first_name','nike_name','last_name','email','date_join','date_update','is_active','is_staff','avatar')
class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model=ForumsPost
            fields=('id','user','title','content','date_created','date_update','likes','dislike')
class PostImageSerializer(serializers.ModelSerializer):
        class Meta:
            model=ForumsPostImage
            fields=('id','post','images')
class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model=ForumsComments
            fields=('id','user','post','comment_content','date_created','date_update')
class CommentsImagesSerializer(serializers.ModelSerializer):
        class Meta:
            model=ForumCommentsImages
            fields=('id','cooment','images')