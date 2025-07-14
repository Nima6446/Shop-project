from django.db import models
from account_module.models import User
from product_module.models import product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return f'Order#{self.id}by{self.user.username}'

    def calculate_total_price(self):
        total_amount = 0
        for order_detail in self.orderdetail_set.all():
            price = order_detail.final_price if self.is_paid else order_detail.product.price
            count = order_detail.count

            # چک می‌کنیم که None نباشن
            if price is not None and count is not None:
                total_amount += price * count

        return total_amount


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return f'{self.product} x {self.count}(Order#{self.order.id})'

    class Meta:
        verbose_name = 'جزییات سلد خرید'
        verbose_name_plural = 'لیست جزییات سبد های خرید'
