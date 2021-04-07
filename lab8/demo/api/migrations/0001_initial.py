# Generated by Django 2.0 on 2021-04-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(max_length=300)),
                ('count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
