# Generated by Django 5.0.3 on 2024-05-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppEcommerce", "0011_remove_product_brand"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Brand",
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(
                choices=[("bina", "bina"), ("müstakil", "müstakil")],
                max_length=50,
                null=True,
            ),
        ),
    ]
