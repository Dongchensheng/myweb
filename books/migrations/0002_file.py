# Generated by Django 2.1.5 on 2019-03-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('fileway', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]