# Generated by Django 2.0.3 on 2018-04-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoisin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='online',
        ),
    ]