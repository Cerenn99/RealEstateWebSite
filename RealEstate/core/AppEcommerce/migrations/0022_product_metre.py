# Generated by Django 5.0.3 on 2024-05-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppEcommerce", "0021_product_adres"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="metre",
            field=models.IntegerField(null=True),
        ),
    ]
