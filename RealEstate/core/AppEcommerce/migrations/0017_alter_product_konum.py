# Generated by Django 5.0.3 on 2024-05-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppEcommerce", "0016_alter_product_konum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="konum",
            field=models.TextField(null=True),
        ),
    ]
