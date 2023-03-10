# Generated by Django 4.1.6 on 2023-02-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'cliente',
            '0005_cliente_numerowhatazapp_cliente_dd_cliente_email_and_more',
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='NumeroWhatazapp',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='dd',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='numero_celula',
        ),
        migrations.AddField(
            model_name='cliente',
            name='celular',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='what',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(
                choices=[
                    ('M', 'Masculino'),
                    ('F', 'Feminino'),
                    ('O', 'Outros'),
                ],
                default='M',
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='situacao',
            field=models.CharField(
                choices=[('A', 'Ativo'), ('I', 'Inativo')],
                default='A',
                max_length=1,
            ),
        ),
    ]
