# Generated by Django 5.0.6 on 2024-07-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyshop', '0003_alter_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
