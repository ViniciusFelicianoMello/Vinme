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
        ("VINME", "Vinme"),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField(blank=False, null=False)
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

class ContentSection(models.Model):
    post = models.ForeignKey(Post, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    text_block = models.TextField(blank=True, null=True)
    images_or_videos1 = models.FileField(upload_to='media/', blank=True, null=True)
    images_or_videos2 = models.FileField(upload_to='media/', blank=True, null=True)
    images_or_videos3 = models.FileField(upload_to='media/', blank=True, null=True)
    images_or_videos4 = models.FileField(upload_to='media/', blank=True, null=True)
    images_or_videos5 = models.FileField(upload_to='media/', blank=True, null=True)
    
    def __str__(self):
        return f"Section: {self.title} in {self.post.title}"

    class Meta:
        verbose_name_plural = "Content Sections"
    

class Comment(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True) 
    rating = models.PositiveIntegerField(
        choices=RATING_CHOICES, 
        validators=[MinValueValidator(1), MaxValueValidator(5)], 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"