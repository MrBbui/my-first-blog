from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
	posts = Post.objects.filteR(published_date_lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
	
	