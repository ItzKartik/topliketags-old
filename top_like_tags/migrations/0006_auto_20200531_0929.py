# Generated by Django 3.0.6 on 2020-05-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_like_tags', '0005_auto_20200531_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_posts',
            name='desc',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_posts',
            name='keyword',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_posts',
            name='seotitle',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
    ]
