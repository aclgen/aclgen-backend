# Generated by Django 4.0.3 on 2022-05-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('id', 'repository')},
        ),
    ]
