from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_avg_rating(self):
        reviews = Review.objects.filter(postz=self)
        count = len(reviews) or 1
        sum = 0
        for rvw in reviews:
            sum += rvw.general_rate
        return sum/count or ' '

class Review(models.Model):
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postz = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, blank=True)
    honesty_rate = models.IntegerField()
    focus_rate = models.IntegerField()
    ambition_rate = models.IntegerField()
    respect_rate = models.IntegerField()
    persuasiveness_rate = models.IntegerField()
    general_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)