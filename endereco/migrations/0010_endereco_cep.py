# Generated by Django 4.1.6 on 2023-02-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0009_alter_endereco_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Cep',
            field=models.CharField(
                default='',
                help_text='Cep da Residencia',
                max_length=9,
                verbose_name='Cep',
            ),
            preserve_default=False,
        ),
    ]
