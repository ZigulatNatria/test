# Generated by Django 3.2.9 on 2022-10-28 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_infouser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infouser',
            name='over_18',
        ),
    ]