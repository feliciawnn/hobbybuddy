# Generated by Django 3.2.5 on 2021-07-17 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity', '0003_alter_activity_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Activity',
            },
        ),
        migrations.AddConstraint(
            model_name='useractivity',
            constraint=models.UniqueConstraint(fields=('user', 'activity'), name='unique user activity'),
        ),
    ]
