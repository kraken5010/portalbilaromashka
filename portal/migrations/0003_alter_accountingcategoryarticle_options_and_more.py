# Generated by Django 4.0 on 2022-01-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_accountingcategoryarticle_itcategoryarticle_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountingcategoryarticle',
            options={'ordering': ['id'], 'verbose_name_plural': '<<Бухгалтерія категорії>>'},
        ),
        migrations.AlterModelOptions(
            name='itcategoryarticle',
            options={'ordering': ['id'], 'verbose_name_plural': '<<IT категорії>>'},
        ),
        migrations.RemoveField(
            model_name='accountingcategoryarticle',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='department',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='itcategoryarticle',
            name='slug',
        ),
    ]
