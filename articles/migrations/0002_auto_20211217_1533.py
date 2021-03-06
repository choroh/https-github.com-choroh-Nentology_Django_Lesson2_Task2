# Generated by Django 3.2.9 on 2021-12-17 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleThema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themas', to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Thema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thema', models.CharField(max_length=70, verbose_name='Тема')),
                ('articles', models.ManyToManyField(through='articles.ArticleThema', to='articles.Article')),
            ],
        ),
        migrations.AddField(
            model_name='articlethema',
            name='thema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.thema', verbose_name='Раздел'),
        ),
    ]
