# Generated by Django 4.1.6 on 2023-02-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='nome',
            field=models.CharField(
                default='',
                help_text='Nome Completo do Departanento',
                max_length=80,
                verbose_name='Nome do Departamento',
            ),
            preserve_default=False,
        ),
    ]
