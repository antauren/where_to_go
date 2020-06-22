# Generated by Django 3.0.7 on 2020-06-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Позиция'),
        ),
    ]