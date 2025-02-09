# Generated by Django 5.0.3 on 2024-03-17 20:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="Brand Image")),
            ],
            options={
                "verbose_name_plural": "Markalar",
            },
        ),
        migrations.CreateModel(
            name="CaseShape",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("case_shape", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Kasa Şekilleri",
            },
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Renkler",
            },
        ),
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gender", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Cinsiyetler",
            },
        ),
        migrations.CreateModel(
            name="GlassFeature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("glass_feature", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Cam Özellikleri",
            },
        ),
        migrations.CreateModel(
            name="Mechanism",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mechanism", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Mekanizmalar",
            },
        ),
        migrations.CreateModel(
            name="StrapType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("strap_type", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Kayış Tipleri",
            },
        ),
        migrations.CreateModel(
            name="Style",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("style", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Tarzlar",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="Product Image")),
                ("price", models.FloatField()),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.brand",
                    ),
                ),
                (
                    "case_shape",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.caseshape",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.color",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.gender",
                    ),
                ),
                (
                    "glass_feature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.glassfeature",
                    ),
                ),
                (
                    "mechanism",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.mechanism",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "strap_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.straptype",
                    ),
                ),
                (
                    "tarz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppEcommerce.style",
                    ),
                ),
            ],
        ),
    ]
