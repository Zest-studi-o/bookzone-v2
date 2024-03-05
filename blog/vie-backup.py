from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    """
    List of post
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')  
    template_name = 'blog/blog.html'  
    paginate_by = 6  


class PostDetail(View):
    """
    Blog post
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)  
        post = get_object_or_404(queryset, slug=slug)  
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True  

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )  

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)  
        post = get_object_or_404(queryset, slug=slug)  
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True  

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )  


class PostLike(View):
    """
    Post likes
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)  

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user) 
        else:
            post.likes.add(request.user) 

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))  


@login_required
def add_post(request):
    """
    To create a post
    """
    form = PostForm(request.POST, request.FILES)

    if request.user.is_superuser:
        if request.method == 'POST':

            if form.is_valid():

                post = form.save(commit=False)
                post.save()
                form = PostForm()
                messages.success(request, 'Successfully created post')
                return redirect('post_detail', post.slug)
            else:
                messages.error(request, 'Failed to add post. Please ensure the form is valid.')  # noqa E501

        template = 'blog/post_add.html'
        context = {
            'form': form,
        }

        return render(request, template, context)

    else:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))


@login_required
def update_post(request, slug):
    """ To update a post """

    post = get_object_or_404(Post, slug=slug)

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated post!')
                return redirect(reverse('blog'))
            else:
                messages.error(request, 'Failed to update the post. Please ensure the form is valid.')  # noqa E501
        else:
            form = PostForm(instance=post)
            messages.info(request, f'You are updating {post.title}')

        template = 'blog/post_edit.html'
        context = {
            'form': form,
            'post': post,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))


@login_required
def delete_post(request, slug):
    """ To delete a post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))