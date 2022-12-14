

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.validators import FileExtensionValidator
from django.db import models


from config.services import crop_center, crop_center_v2
from users.models import CustomUser

from moviepy.editor import VideoFileClip

User = get_user_model()



# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Video(models.Model):
    title = models.CharField(max_length=130, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='vid/image/%Y/%m/%d/',null=True, blank=True, verbose_name="Постер")
    file = models.FileField(
        upload_to='vid/video/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', "mkv", "DVR", 'Mov', 'mov'])], verbose_name="Файл"
    )
    duration = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE, verbose_name="Канал")
    category = models.ManyToManyField(Category, related_name="category", verbose_name="Категории", blank=True)
    views = models.ManyToManyField(User, through='Views', verbose_name="Просмотры")
    likes = models.ManyToManyField(User, related_name='likes', through="Likes", verbose_name="Лайки")

    def __str__(self):
        return self.title

    def get_count_views(self):
        return self.views.count()

    def get_count_likes(self):
        return self.likes.count()



    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Views(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="view_user")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="view_video")
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time',)
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'video'], name='unique_migrationViews_user_video'
            )
        ]


class Likes(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='video', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'video'], name='unique_migrationLikes_user_video'
            )
        ]



class Channel(models.Model):
    class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"


    def __str__(self):
        return f"{self.user.id}-{self.name}"

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40, default="Channel Name")
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='channel/image/profile/image/%Y/%m/', null=True, blank=True)
    banner = models.ImageField(upload_to='channel/image/profile/banner/%Y/%m/', null=True, blank=True)
    logo = models.ImageField(upload_to='channel/image/profile/logo/%Y/%m/', null=True, blank=True)
    is_active = models.BooleanField(default=0)
    subscribers = models.ManyToManyField(User, through="Subscribers", related_name='subs')

    def get_count_subscribes(self):
        return self.subscribers.count()

    def save(self, *args, **kwargs):
        super(Channel, self).save(*args, **kwargs)
        if self.logo:
            image = Image.open(self.logo.path)
            image = crop_center_v2(image, (1, 1))
            image.save(self.logo.path)


class Subscribers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_user')
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE, related_name='sub_channel')

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'channel'], name='unique_migrationSubscribers_user_channel'
            )
        ]



