# Generated by Django 4.1.7 on 2023-03-30 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0010_endereco_cep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='Bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Complem',
            new_name='complemento',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Logradouro',
            new_name='logradouro',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Nome_do_Logradouro',
            new_name='nome_do_logradouro',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='Numero',
            new_name='numero',
        ),
    ]
