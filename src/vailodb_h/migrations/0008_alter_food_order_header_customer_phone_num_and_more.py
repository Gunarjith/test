# Generated by Django 4.2.3 on 2024-02-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0007_serivce_order_food_order_header_food_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_order_header',
            name='customer_phone_num',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='serivce_order',
            name='customer_phone_num',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
