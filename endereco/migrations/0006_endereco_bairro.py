# Generated by Django 4.1.6 on 2023-02-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0005_endereco_complem'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Bairro',
            field=models.CharField(default='', help_text='Bairro da Residencia', max_length=70, verbose_name='Bairro'),
            preserve_default=False,
        ),
    ]
