# Generated by Django 3.2 on 2022-04-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]