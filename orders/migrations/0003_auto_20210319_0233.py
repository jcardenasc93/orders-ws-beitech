# Generated by Django 3.1 on 2021-03-19 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210319_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=0, max_length=999999999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_description',
            field=models.CharField(blank=True, max_length=191),
        ),
    ]
