# Generated by Django 5.0.7 on 2024-07-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
