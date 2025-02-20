# Generated by Django 5.0.3 on 2024-03-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salary", "0002_vacancy_desc_vacancy_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vacancy",
            options={"verbose_name_plural": "Vacancies"},
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="salary",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
