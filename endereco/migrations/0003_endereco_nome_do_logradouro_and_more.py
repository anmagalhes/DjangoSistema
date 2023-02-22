# Generated by Django 4.1.6 on 2023-02-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_endereco_logradouro'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Nome_do_Logradouro',
            field=models.CharField(default='', help_text='Nome do Logradouro', max_length=70, verbose_name='Nome do Logradouro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='Logradouro',
            field=models.CharField(choices=[('Rua', 'Rua'), ('Avenida', 'Avenida'), ('Praca', 'Praca'), ('Estrada', 'Estrada'), ('Travessa', 'Travessa'), ('Viela', 'Viela'), ('Passagem', 'Passagem')], default='Rua', help_text='Nome do Logradouro', max_length=9, verbose_name='Logradouro'),
        ),
    ]
