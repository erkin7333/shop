from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from io import BytesIO
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Category"


class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'
    STATUS_CHOCES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Delated')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product/thumbnail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOCES, default=ACTIVE)
    def __str__(self):
        return self.title
    def get_diplay_price(self):
        return self.price / 100

    def make_thumbnail(self, image, size=(1000, 1000)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
        thumbnail = File(thumb_io, name=name)
        return thumbnail

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fpython-crash-course%2F&psig=AOvVaw0YGRHVX6I6UVvgOuqmtYom&ust=1669789846547000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPDm1Ybi0vsCFQAAAAAdAAAAABAE'

    class Meta:
        verbose_name = "Maxsulot"
        ordering = ('-created_at',)


