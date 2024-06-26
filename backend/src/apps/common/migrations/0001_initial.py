# Generated by Django 5.0.6 on 2024-05-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hash', models.UUIDField(null=True, unique=True)),
                ('path', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'apps:common:image:verbose',
                'verbose_name_plural': 'apps:common:image:verbose-plural',
                'db_table': 'image',
            },
        ),
    ]
