# Generated by Django 2.1.5 on 2019-04-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20190424_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='cahegory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='document',
            name='number',
            field=models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='Порядок сортировки'),
        ),
    ]