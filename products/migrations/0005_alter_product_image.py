# Generated by Django 5.1 on 2024-08-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/products/"),
        ),
    ]
