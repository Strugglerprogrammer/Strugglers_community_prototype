from django.contrib import admin
from .models import Profile, Forum, Thread, Post

admin.site.register(Profile)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
