# Generated by Django 3.2.9 on 2021-12-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20211218_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlethema',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='thema',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterField(
            model_name='thema',
            name='thema',
            field=models.CharField(max_length=50, verbose_name='Тема'),
        ),
        migrations.AlterUniqueTogether(
            name='articlethema',
            unique_together={('article', 'thema')},
        ),
    ]
