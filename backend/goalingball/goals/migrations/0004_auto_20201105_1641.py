# Generated by Django 3.1.2 on 2020-11-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_goal_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
    ]
