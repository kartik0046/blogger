# Generated by Django 3.1.4 on 2021-01-12 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20210112_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(related_name='downvote', to=settings.AUTH_USER_MODEL),
        ),
    ]
