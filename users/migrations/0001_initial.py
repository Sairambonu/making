# Generated by Django 4.2.3 on 2023-10-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginInfo',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('email', models.CharField(max_length=50, unique=True)),
                ('role', models.CharField(default='annotator', max_length=20)),
                ('phone', models.CharField(default='', max_length=12)),
                ('languages', models.CharField(default='telugu', max_length=100)),
                ('status', models.CharField(default='active', max_length=10)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
