# Generated by Django 4.1.2 on 2022-10-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v', '0003_clipboard_expire_date_clipboard_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clipboard',
            old_name='idd',
            new_name='id',
        ),
    ]
