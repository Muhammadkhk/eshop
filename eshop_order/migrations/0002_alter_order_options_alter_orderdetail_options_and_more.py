# Generated by Django 4.0.3 on 2022-04-03 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_alter_product_options_alter_productgallery_options_and_more'),
        ('eshop_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderdetail',
            options={},
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_order.order'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product'),
        ),
    ]
