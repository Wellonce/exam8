# Generated by Django 5.0.3 on 2024-03-30 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Round",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sport",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("username", models.CharField(max_length=128)),
                ("password", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="League",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
                ("cover", models.ImageField(upload_to="media")),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.sport"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=100)),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.sport"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Statistics",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "team_id",
                    models.ManyToManyField(related_name="statistics", to="task4.team"),
                ),
            ],
            options={
                "verbose_name": "Statistics",
                "verbose_name_plural": "Statistics",
            },
        ),
        migrations.CreateModel(
            name="Points",
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
                ("points", models.IntegerField(default=0)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.team"
                    ),
                ),
            ],
            options={
                "verbose_name": "Points",
                "verbose_name_plural": "Points",
            },
        ),
        migrations.CreateModel(
            name="Match",
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
                ("date", models.DateTimeField()),
                ("score", models.CharField(blank=True, max_length=10, null=True)),
                ("status", models.CharField(default="Not Started", max_length=20)),
                ("live", models.BooleanField(default=False)),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.sport"
                    ),
                ),
                (
                    "away_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="away_matches",
                        to="task4.team",
                    ),
                ),
                (
                    "home_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_matches",
                        to="task4.team",
                    ),
                ),
            ],
        ),
    ]