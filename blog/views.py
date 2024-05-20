# Create your views here.
from django.shortcuts import render
#from hitcount.views import HitCountDetailView
from blog.models import Post, Organism
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil

def home(request):
    posts = Post.objects.all()[0:6]
    return render(request, 'home.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post.html', {'post': post,
                                         'comments': comments,
                                         'new_comment':new_comment,
                                         'comment_form':comment_form})

def publicacoes(request):
    return render(request, "publicacoes.html")

def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts, page:'pages'})

def OrganismView(request, organisms):
    organism_posts = Post.objects.filter(organism=organisms)
    return render(request, "organism.html", {"organisms": organisms, 'organism_posts': organism_posts})
