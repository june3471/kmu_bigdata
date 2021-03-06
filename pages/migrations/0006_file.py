# Generated by Django 2.1.3 on 2018-11-15 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20181115_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_title', models.CharField(max_length=50)),
                ('f_contents', models.TextField()),
                ('f_date', models.DateTimeField(verbose_name='date published')),
                ('f_short_intro', models.CharField(max_length=100)),
                ('f_file', models.FileField(upload_to='uploads/')),
                ('f_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('b_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Boards')),
                ('b_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Board_menu')),
            ],
        ),
    ]
