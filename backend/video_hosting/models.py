from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser

User = get_user_model()
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/')
    file = models.FileField(
        upload_to='video/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', "mvk"])],

    )
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey("Channel", verbose_name="Канал", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    views = models.ManyToManyField(User, through='Views')

    def __str__(self):
        return self.title

    def get_count_views(self):
        return self.views.count()
    class Meta:
        ordering = ('-created_at',)

class Views(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_id")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

class Channel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40, default="Channel Name")
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='image/profile/image/%Y/%m/', null=True)
    banner = models.ImageField(upload_to='image/profile/banner/%Y/%m/', null=True)
    logo = models.ImageField(upload_to='image/profile/logo/%Y/%m/', null=True)
    is_active = models.BooleanField(default=0)


@receiver(post_save, sender=CustomUser)
def create_user_channel(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_channel(sender, instance, **kwargs):
    instance.channel.save()
