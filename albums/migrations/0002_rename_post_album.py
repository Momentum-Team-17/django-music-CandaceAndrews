# Generated by Django 4.1.7 on 2023-02-27 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Album',
        ),
    ]
