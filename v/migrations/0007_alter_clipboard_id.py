# Generated by Django 4.1.2 on 2022-10-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v', '0006_reporter_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboard',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
