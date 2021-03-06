# Generated by Django 4.0.3 on 2022-04-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_alter_product_options_alter_productgallery_options_and_more'),
        ('eshop_tag', '0002_auto_20200701_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.AlterField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.product'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
