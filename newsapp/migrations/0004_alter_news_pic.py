# Generated by Django 4.0.5 on 2022-09-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_alter_news_newsdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.ImageField(default='news-image.jpg', upload_to=''),
        ),
    ]