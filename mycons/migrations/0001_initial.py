# Generated by Django 4.1.1 on 2022-09-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=122)),
                ('zip', models.CharField(max_length=10)),
            ],
        ),
    ]