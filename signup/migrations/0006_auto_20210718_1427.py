# Generated by Django 3.1.6 on 2021-07-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
