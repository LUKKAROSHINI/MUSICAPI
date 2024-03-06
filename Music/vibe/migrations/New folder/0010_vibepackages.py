# Generated by Django 5.0.2 on 2024-02-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibe', '0009_delete_vibepackages'),
    ]

    operations = [
        migrations.CreateModel(
            name='VibePackages',
            fields=[
                ('musicid', models.AutoField(primary_key=True, serialize=False)),
                ('musiccode', models.CharField(max_length=10)),
                ('musictitle', models.CharField(max_length=30)),
                ('musicPackage', models.CharField(max_length=30)),
                ('musicdescription', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'Package_table',
            },
        ),
    ]
