# Generated by Django 4.2.7 on 2023-11-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.EmailField(default='none@none.no', max_length=254),
            preserve_default=False,
        ),
    ]
