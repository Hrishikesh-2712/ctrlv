# Generated by Django 4.1.2 on 2022-10-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v', '0004_rename_idd_clipboard_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clipboard',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='clipboard',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
