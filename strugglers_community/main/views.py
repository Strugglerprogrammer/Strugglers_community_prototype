from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Forum, Thread, Post
from .forms import UserForm, ProfileForm, ThreadForm, PostForm, ForumForm, SearchForm 
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    forums = Forum.objects.all()
    return render(request, 'main/index.html', {'forums': forums})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Forum.objects.filter(title=title).exists():
                messages.error(request, 'Forum with this title already exists.')
            else:
                form.save()
                messages.success(request, 'Forum created successfully!')
                return redirect('main:forum_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ForumForm()
    return render(request, 'main/create_forum.html', {'form': form})


@login_required
def create_thread(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id, user = request.user)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum = forum
            thread.created_by = request.user
            thread.save()
            messages.success(request, 'Thread created successfully!')
            return redirect('main:post_list', thread_id=thread.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ThreadForm()
    return render(request, 'main/create_thread.html', {'form': form, 'forum': forum})

@login_required
def create_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('main:post_list', thread_id=thread.id)
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})



def forum_list(request):
    forums = Forum.objects.all().order_by('-created_at')
    return render(request, 'main/forums.html', {'forums': forums})



def thread_list(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    threads = Thread.objects.filter(forum=forum)
    paginator = Paginator(threads, 10)  # 10 threads per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/threads.html', {'forum': forum, 'page_obj': page_obj})

def post_list(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = Post.objects.filter(thread=thread)
    paginator = Paginator(posts, 10)  # 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/posts.html', {'thread': thread, 'page_obj': page_obj})

def search(request):
    query = request.GET.get('query')
    threads = Thread.objects.filter(Q(title__icontains=query))
    posts = Post.objects.filter(Q(content__icontains=query))
    return render(request, 'main/search_results.html', {'threads': threads, 'posts': posts, 'query': query})

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('main:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'main/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })