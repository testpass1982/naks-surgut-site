# Generated by Django 2.1.5 on 2019-04-25 05:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20190425_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название вставки')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Форматирование вставки')),
            ],
            options={
                'verbose_name_plural': 'Вставки',
                'verbose_name': 'Вставка',
            },
        ),
    ]