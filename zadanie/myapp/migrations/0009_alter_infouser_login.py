# Generated by Django 3.2.9 on 2022-10-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20221029_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='login',
            field=models.CharField(max_length=50),
        ),
    ]
