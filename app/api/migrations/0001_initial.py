# Generated by Django 4.0.3 on 2022-05-07 17:57

import app.api.enums
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(max_length=255)),
                ('type', models.CharField(choices=[('FIREWALL', 'FIREWALL'), ('CLUSTER', 'CLUSTER')], default=app.api.enums.DeviceType['FIREWALL'], max_length=64)),
            ],
            options={
                'verbose_name': 'Device',
            },
        ),
        migrations.CreateModel(
            name='DeviceFolder',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='api.device')),
            ],
            options={
                'verbose_name': 'Device Folder',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=32)),
                ('comment', models.TextField(max_length=255)),
                ('range_start', models.TextField(max_length=64)),
                ('range_end', models.TextField(max_length=64)),
                ('lock', models.CharField(choices=[('LOCKED', app.api.enums.LockStatus['LOCKED']), ('UNLOCKED', app.api.enums.LockStatus['UNLOCKED'])], default=app.api.enums.LockStatus['UNLOCKED'], max_length=64)),
            ],
            options={
                'verbose_name': 'Object',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=64)),
            ],
            options={
                'verbose_name': 'Repository',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('icmp_type', models.PositiveSmallIntegerField(blank=True)),
                ('icmp_code', models.PositiveSmallIntegerField(blank=True)),
                ('port_start', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('port_end', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('protocol', models.CharField(blank=True, choices=[('TCP', 'TCP'), ('UDP', 'UDP'), ('ICMP', 'ICMP')], max_length=64)),
                ('name', models.TextField(max_length=128)),
                ('comment', models.TextField(max_length=255)),
                ('type', models.CharField(choices=[('ICMP', 'ICMP'), ('PORT', 'PORT'), ('COLLECTION', 'COLLECTION')], max_length=65)),
                ('lock', models.CharField(blank=True, choices=[('LOCKED', app.api.enums.LockStatus['LOCKED']), ('UNLOCKED', app.api.enums.LockStatus['UNLOCKED'])], default=app.api.enums.LockStatus['UNLOCKED'], max_length=64)),
                ('members', models.ManyToManyField(blank=True, to='api.service')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.repository')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=64)),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('direction', models.CharField(choices=[('INBOUND', 'INBOUND'), ('OUTBOUND', 'OUTBOUND')], default=app.api.enums.RuleDirection['INBOUND'], max_length=64)),
                ('action', models.CharField(choices=[('ACCEPT', 'ACCEPT'), ('DENY', 'DENY')], default=app.api.enums.RuleAction['ACCEPT'], max_length=64)),
                ('destinations', models.ManyToManyField(related_name='rule_destinations', to='api.object')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='api.device')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rule_folders', to='api.devicefolder')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.repository')),
                ('services_destinations', models.ManyToManyField(blank=True, null=True, related_name='rule_services_destination', to='api.service')),
                ('services_sources', models.ManyToManyField(blank=True, null=True, related_name='rule_services_source', to='api.service')),
                ('sources', models.ManyToManyField(related_name='rule_sources', to='api.object')),
            ],
            options={
                'verbose_name': 'Rule',
            },
        ),
        migrations.AddField(
            model_name='object',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectlist', to='api.repository'),
        ),
        migrations.AddField(
            model_name='device',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='api.repository'),
        ),
    ]
