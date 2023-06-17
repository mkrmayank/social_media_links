# Generated by Django 4.0.5 on 2022-07-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='media/')),
                ('name', models.CharField(default='', max_length=122)),
                ('number', models.CharField(max_length=12)),
                ('designation', models.TextField()),
                ('social1', models.CharField(default='', max_length=122)),
                ('social2', models.CharField(default='', max_length=122)),
                ('social3', models.CharField(default='', max_length=122)),
                ('social4', models.CharField(default='', max_length=122)),
                ('social5', models.CharField(default='', max_length=122)),
            ],
        ),
    ]