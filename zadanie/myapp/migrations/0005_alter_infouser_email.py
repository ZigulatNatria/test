# Generated by Django 3.2.9 on 2022-10-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20221029_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]