# Generated by Django 4.2.5 on 2023-09-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('location', models.TextField()),
            ],
        ),
    ]
