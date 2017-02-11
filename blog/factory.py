from django.utils import lorem_ipsum
from .models import Post

def create_some_posts(number):
    for i in range(number):
        post = Post()
        post.title = 'Topic {}'.format(i)
        post.text = lorem_ipsum.paragraph()
        post.author = 'bog'
        post.save()
        
def remove_default_topics():
    posts = Post.objects.filter(title__startswith('Topic '))
    print('Removing {} posts').format(posts.count())
    posts.delete()