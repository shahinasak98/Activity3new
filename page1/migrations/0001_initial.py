# Generated by Django 4.1 on 2022-08-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputnum', models.IntegerField(max_length=100)),
                ('outputword', models.CharField(max_length=1000)),
            ],
        ),
    ]