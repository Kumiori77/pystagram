# Generated by Django 4.2.5 on 2023-12-21 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_like_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='like_post',
            new_name='like_posts',
        ),
    ]