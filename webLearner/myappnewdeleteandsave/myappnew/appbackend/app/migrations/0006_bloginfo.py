# Generated by Django 4.1.1 on 2022-11-30 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('blogdata', models.CharField(max_length=200000)),
            ],
        ),
    ]
