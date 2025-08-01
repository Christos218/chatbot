# Generated by Django 4.1.9 on 2023-05-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100, null=True)),
                ('conversation', models.TextField()),
                ('user_timestamp', models.DateTimeField(auto_now_add=True)),
                ('bot_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
