# Generated by Django 4.0.3 on 2022-04-01 09:59

import app.object.models
import app.rules.enums
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('object', '0006_alter_object_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleSet',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Ruleset',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('service', models.TextField(max_length=255)),
                ('direction', models.CharField(choices=[('INBOUND', 'INBOUND'), ('OUTBOUND', 'OUTBOUND')], default=app.rules.enums.Direction['INBOUND'], max_length=64)),
                ('action', models.CharField(choices=[('ACCEPT', 'ACCEPT'), ('DENY', 'DENY')], default=app.rules.enums.Action['ACCEPT'], max_length=64)),
                ('destination', models.ForeignKey(on_delete=models.SET(app.object.models.Object.get_deleted_object_dummy), related_name='destination', to='object.object')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='rules.ruleset')),
                ('source', models.ForeignKey(on_delete=models.SET(app.object.models.Object.get_deleted_object_dummy), related_name='source', to='object.object')),
            ],
            options={
                'verbose_name': 'Rule',
            },
        ),
    ]
