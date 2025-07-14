
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='نام برند')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(verbose_name='Active / Inactive'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_delete',
            field=models.BooleanField(verbose_name='Delete / Undelete'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='url_title',
            field=models.CharField(db_index=True, max_length=300, verbose_name='URL Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_category', to='product_module.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(db_index=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(verbose_name='Delete / Undelete'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(db_index=True, max_length=360, null=True, verbose_name='Short_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='products_tags',
            name='caption',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.product_brand', verbose_name='برند'),
        ),
    ]
