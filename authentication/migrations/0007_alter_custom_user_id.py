# Generated by Django 3.2.4 on 2021-12-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20211229_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]