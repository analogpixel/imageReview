# Generated by Django 5.1.1 on 2024-09-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0002_image_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('images', models.ManyToManyField(related_name='days', to='review_app.image')),
            ],
        ),
    ]
