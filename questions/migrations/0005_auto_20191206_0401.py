# Generated by Django 3.0 on 2019-12-06 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20191206_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='questions.Theme'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='nom',
            field=models.CharField(default='Inconnu', max_length=64),
        ),
    ]
