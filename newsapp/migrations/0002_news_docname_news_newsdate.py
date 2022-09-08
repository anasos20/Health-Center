# Generated by Django 4.0.5 on 2022-09-08 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='docname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor'),
        ),
        migrations.AddField(
            model_name='news',
            name='newsdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
