# Generated by Django 4.0.3 on 2022-06-21 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TheMoreYouKnow', '0003_content_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
