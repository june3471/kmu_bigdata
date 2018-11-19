# Generated by Django 2.1.3 on 2018-11-15 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='b_title',
        ),
        migrations.AddField(
            model_name='boards',
            name='f_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.File'),
        ),
    ]