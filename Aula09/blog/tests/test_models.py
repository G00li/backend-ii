import pytest
from django.utils import timezone
from blog.models import BlogPost
from factory import Faker
from factory.django import DjangoModelFactory

class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost
    
    title = Faker('sentence')
    content = Faker('paragraph')
    author = Faker('name')

@pytest.mark.django_db
class TestBlogPost:
    def test_create_blog_post(self):
        post = BlogPostFactory()
        assert post.title is not None
        assert post.content is not None
        assert post.author is not None
        assert post.published_date is not None
    
    def test_str_representation(self):
        post = BlogPostFactory(title="Test Post")
        assert str(post) == "Test Post"
    
    def test_publish_method(self):
        post = BlogPostFactory()
        old_date = post.published_date
        post.publish()
        assert post.published_date > old_date
    
    def test_get_summary_short_content(self):
        post = BlogPostFactory(content="Short content")
        assert post.get_summary() == "Short content"
    
    def test_get_summary_long_content(self):
        long_content = "This is a very long content that should be truncated " * 10
        post = BlogPostFactory(content=long_content)
        summary = post.get_summary()
        assert len(summary) == 100
        assert summary.endswith("...")
    
    @pytest.mark.parametrize("max_length", [50, 100, 200])
    def test_get_summary_different_lengths(self, max_length):
        content = "This is a test content " * 10
        post = BlogPostFactory(content=content)
        summary = post.get_summary(max_length=max_length)
        assert len(summary) <= max_length + 3  # +3 for "..." 