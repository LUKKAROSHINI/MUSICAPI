# Generated by Django 5.0.1 on 2024-02-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibe', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='VibeRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(default='Unknown', max_length=30)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('phno', models.CharField(max_length=15, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'musicregister_table',
            },
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]