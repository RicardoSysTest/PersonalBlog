from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Post(models.Model):
    
    #Those are the Values sotre in the DB
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    #Those are the values that we will see in the Frontend
    CHOICE_STATUS = (
        (ACTIVE,'Active'),
        (DRAFT,'Draft'),
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default=DRAFT)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    #Sort the Data to display first the most recent
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):

    #When you delete a post you delete all the comments related to this post
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
