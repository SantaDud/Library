# Generated by Django 3.2.5 on 2021-08-03 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books', '0006_auto_20210731_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='issuedTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issuedBooks', to=settings.AUTH_USER_MODEL),
        ),
    ]
