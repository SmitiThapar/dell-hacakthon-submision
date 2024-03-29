from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    product_id = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name + " " + str(self.product_id)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Service(models.Model):
    product = models.OneToOneField(Product, default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default="")
    description = models.TextField(blank=True)
    service_id = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:service_page',
                       args=[self.id, self.slug])


class Support(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(max_length=400, db_index=True, default="")
    description = models.TextField(blank=True)
    support_id = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:support_page',
                       args=[self.id, self.slug])


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(blank=True)
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name + " " + str(self.rating)
