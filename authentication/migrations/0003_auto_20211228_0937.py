# Generated by Django 3.1.3 on 2021-12-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20211228_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]