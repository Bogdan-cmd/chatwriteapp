# Generated by Django 3.1.7 on 2021-06-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(verbose_name='Titlu'),
        ),
    ]
