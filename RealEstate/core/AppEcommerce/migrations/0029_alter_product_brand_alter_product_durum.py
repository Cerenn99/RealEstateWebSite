# Generated by Django 5.0.3 on 2024-06-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppEcommerce", "0028_alter_product_brand_alter_product_durum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.CharField(
                choices=[("bina", "bina"), ("müstakil", "müstakil")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="durum",
            field=models.CharField(
                choices=[("kiralık", "kiralık"), ("satılık", "satılık")],
                max_length=50,
                null=True,
            ),
        ),
    ]
