# Generated by Django 5.0.4 on 2024-05-08 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userfollowing_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user', 'following_user')},
        ),
    ]