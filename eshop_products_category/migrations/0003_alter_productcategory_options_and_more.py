# Generated by Django 4.0.3 on 2022-04-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_auto_20200701_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]