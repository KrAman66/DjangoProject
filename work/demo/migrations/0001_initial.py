# Generated by Django 3.1 on 2021-05-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('mark', models.FloatField()),
            ],
        ),
    ]
