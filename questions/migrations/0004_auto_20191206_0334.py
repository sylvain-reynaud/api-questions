# Generated by Django 3.0 on 2019-12-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20191206_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='theme',
        ),
    ]
