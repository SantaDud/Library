# Generated by Django 3.2.5 on 2021-07-31 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fine',
            field=models.IntegerField(default=0),
        ),
    ]