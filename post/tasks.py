from celery import shared_task
from post.models import Post


@shared_task
def create_post(title, content):
    Post.objects.create(title=title, content=content)
    return "Post created successfully"
