# Generated by Django 3.0.6 on 2020-05-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_like_tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_posts',
            name='b_url',
            field=models.CharField(default='hey', max_length=100),
            preserve_default=False,
        ),
    ]
