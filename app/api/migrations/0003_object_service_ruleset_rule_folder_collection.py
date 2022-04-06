# Generated by Django 4.0.3 on 2022-04-04 15:34

import app.api.enums
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=32)),
                ('comment', models.TextField(max_length=255)),
                ('range_start', models.TextField(max_length=64)),
                ('range_end', models.TextField(max_length=64)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
            ],
            options={
                'verbose_name': 'Object',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(max_length=255)),
                ('port_start', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('port_end', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('protocol', models.CharField(choices=[('TCP', 'TCP'), ('UDP', 'UDP'), ('ICMP', 'ICMP')], default=app.api.enums.Protocol['UDP'], max_length=64)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
            ],
            options={
                'verbose_name': 'Service',
            },
        ),
        migrations.CreateModel(
            name='RuleSet',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruleset', to='api.device')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
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
                ('direction', models.CharField(choices=[('INBOUND', 'INBOUND'), ('OUTBOUND', 'OUTBOUND')], default=app.api.enums.RuleDirection['INBOUND'], max_length=64)),
                ('action', models.CharField(choices=[('ACCEPT', 'ACCEPT'), ('DENY', 'DENY')], default=app.api.enums.RuleAction['ACCEPT'], max_length=64)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_objects', to='api.object')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='api.ruleset')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.service')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_objects', to='api.object')),
            ],
            options={
                'verbose_name': 'Rule',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.folder')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
            ],
            options={
                'verbose_name': 'Folder',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(max_length=255)),
                ('folder', models.ManyToManyField(related_name='collections', to='api.folder')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository')),
            ],
            options={
                'verbose_name': 'Collection',
            },
        ),
    ]