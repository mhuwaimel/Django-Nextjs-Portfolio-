# Generated by Django 4.2.4 on 2024-02-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="work_place",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
