# Generated by Django 3.1 on 2021-03-19 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210319_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerproduct',
            name='customer_id',
            field=models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='orders.customer'),
        ),
        migrations.AlterField(
            model_name='customerproduct',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='orders.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='orders.customer'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='customer_id',
            field=models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='orders.customer'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='orders.product'),
        ),
    ]