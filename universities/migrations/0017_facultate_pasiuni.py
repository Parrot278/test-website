# Generated by Django 5.1.6 on 2025-03-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("universities", "0016_participareolimpiade_facultate_participare_olimpiade"),
    ]

    operations = [
        migrations.AddField(
            model_name="facultate",
            name="pasiuni",
            field=models.ManyToManyField(blank=True, to="universities.pasiune"),
        ),
    ]
