from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    location = models.CharField(max_length=100, blank=True)  # New field
    website = models.URLField(blank=True)  # New field

    def __str__(self):
        return self.user.username

class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title

class Thread(models.Model):
    forum = models.ForeignKey(Forum, related_name='threads', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['title']),  # Indexing for search optimization
        ]

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['content']),  # Indexing for search optimization
        ]

    def __str__(self):
        return self.content[:50]
