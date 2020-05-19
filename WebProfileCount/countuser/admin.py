from django.contrib import admin
from  .models import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(ForumsPost)
admin.site.register(ForumsPostImage)
admin.site.register(ForumsComments)
admin.site.register(ForumCommentsImages)
