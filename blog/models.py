from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Post(models.Model):
    CATEGORIES = [
        ("FRONT_END", "Front-end"),
        ("BACK_END", "Back-end"),
        ("DESIGN", "Design"),
        ("BUSINESS", "Negócios"),
        ("TUTORIALS", "Tutoriais"),
        ("TECNOLOGIA", "Tecnologia"),
        ("PHOTOGRAPHY", "Fotografia"),
        ("ARTE", "Arte"),
        ("GAMING", "Gaming"),
        ("GEEK", "Geek"),
        ("CINEMA_TV", "Cinema e TV"),
        ("TRAVEL", "Viagem"),
        ("BOOKS", "Livros"),
        ("RECEITAS", "Receitas"),
        ("FASHION", "Moda"),
        ("LIFESTYLE", "Lifestyle"),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='FRONT_END')
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        ratings = self.comments.values_list('rating', flat=True)
        if ratings:
            return sum(ratings) / len(ratings)
        return 0
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

class ContentSection(models.Model):
    post = models.ForeignKey(Post, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text_block = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Section: {self.title} in {self.post.title}"


class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    section = models.ForeignKey(ContentSection, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='content_media/')
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPES)

    def __str__(self):
        return f"Media in {self.section.title} ({self.media_type})"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"