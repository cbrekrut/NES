# Generated by Django 5.0.3 on 2024-04-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0003_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.ImageField(default=0, upload_to='media/'),
            preserve_default=False,
        ),
    ]
