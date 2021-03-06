# Generated by Django 3.0.5 on 2020-05-13 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumsPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField(max_length=87877)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=48)),
                ('first_name', models.CharField(max_length=48, verbose_name='First_Name')),
                ('nike_name', models.CharField(max_length=48, unique=True, verbose_name='Nike_Name')),
                ('last_name', models.CharField(max_length=48, verbose_name='Family_Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('date_join', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='date_update')),
                ('is_active', models.BooleanField(default=True, verbose_name='Account is Active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='is the user among the admin team')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForumsPostImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.ImageField(blank=True, null=True, upload_to='ForumsPostImage/%Y/%m/%d')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countuser.ForumsPost')),
            ],
        ),
        migrations.AddField(
            model_name='forumspost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countuser.MyUser'),
        ),
        migrations.CreateModel(
            name='ForumsComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField(max_length=23232)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_uodate', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countuser.ForumsPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countuser.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='ForumCommentsImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.ImageField(blank=True, null=True, upload_to='ForumCommentsImages')),
                ('cooment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countuser.ForumsComments')),
            ],
        ),
    ]
