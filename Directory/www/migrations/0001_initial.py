# Generated by Django 2.0 on 2017-12-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
