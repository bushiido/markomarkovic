# Generated by Django 4.2.3 on 2023-12-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Vezba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('naziv', models.CharField(default='', max_length=256)),
                ('opis', models.CharField(default='', max_length=16000)),
                ('program', models.IntegerField(default=None)),
            ],
        ),
    ]
