# Generated by Django 5.0.3 on 2024-04-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]