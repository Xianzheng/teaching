# Generated by Django 4.1.1 on 2022-12-04 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_bloginfo_timerecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloginfo',
            name='timeRecord',
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='timerecord',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
