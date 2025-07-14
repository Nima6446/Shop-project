from django.db import models
from django.urls import reverse
from account_module.models import User


class category(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='دسته بندی')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='URL عنوان')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف نشده / حذف شده')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class product_brand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام برند')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return f"{self.title}"


class product(models.Model):
    category = models.ManyToManyField(category, verbose_name='دسته بندی', related_name="product_category")
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(product_brand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    title = models.CharField(max_length=300, db_index=True, verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیجات", db_index=True)
    short_description = models.CharField(max_length=360, null=True, db_index=True, verbose_name="توضیحات کوتاه")
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(verbose_name='حذف نشده / حذف شده')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name="slug")

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class products_tags(models.Model):
    caption = models.CharField(max_length=300, verbose_name='تگ', db_index=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='products_tag')

    class Meta:
        verbose_name = "تگ ها"
        verbose_name_plural = "تگ ها"

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True,verbose_name='کاربر' )

    def __str__(self):
        return f"{self.product.title} / {self.ip}"

    class Meta:
        verbose_name = "بازدید محصول"
        verbose_name_plural = "بازدید های محصول"


class ProductGallery(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/products-gallery',verbose_name='تصویر')


    def __str__(self):
        return self.product.title


    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "گالری تصاویر"

