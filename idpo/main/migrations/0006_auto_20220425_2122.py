# Generated by Django 2.0.13 on 2022-04-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220425_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Название'),
        ),
    ]
