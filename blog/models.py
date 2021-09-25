from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique='created')
    category = models.ManyToManyField(Category, related_name="posts")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    file = models.FileField(null=True, blank=True, upload_to='postimgs/')
    like = models.ManyToManyField(CustomUser, null=True, blank=True, related_name='like')
    dislike = models.ManyToManyField(CustomUser, null=True, blank=True, related_name='dislike')
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = "post"
        verbose_name_plural = "postlar"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            while True:
                try:
                    post = Post.objects.get(slug=slug)
                    if post == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break

        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug, self.created.year, self.created.month, self.created.day, self.created.hour, self.created.minute, self.created.second])