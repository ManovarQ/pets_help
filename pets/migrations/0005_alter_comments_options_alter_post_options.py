# Generated by Django 4.2.7 on 2023-11-30 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_comments_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comments', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Posts', 'verbose_name_plural': 'Posts'},
        ),
    ]