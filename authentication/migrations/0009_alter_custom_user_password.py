# Generated by Django 3.2.4 on 2021-12-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_custom_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]