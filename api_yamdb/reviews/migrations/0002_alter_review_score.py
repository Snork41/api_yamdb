# Generated by Django 3.2 on 2023-05-02 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, message='Оценка должна быть не меньше 1.'), django.core.validators.MaxValueValidator(10, message='Оценка должна быть не больше 10.')], verbose_name='оценка'),
        ),
    ]