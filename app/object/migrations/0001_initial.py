# Generated by Django 4.0.3 on 2022-03-25 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('util', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='util.basemodel')),
                ('name', models.TextField(max_length=32)),
                ('description', models.TextField(max_length=255)),
                ('defs', models.JSONField()),
            ],
            bases=('util.basemodel',),
        ),
    ]
