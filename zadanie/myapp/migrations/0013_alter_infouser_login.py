# Generated by Django 3.2.9 on 2022-10-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_infouser_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='login',
            field=models.CharField(max_length=50),
        ),
    ]
