# Generated by Django 4.1.6 on 2023-02-16 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_cliente_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='CPF',
            field=models.CharField(
                help_text='Número do CPF, Sem traços ou pontos',
                max_length=15,
                verbose_name='Número do CPF',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(
                blank=True,
                help_text='Número do celular com o DDD Sem traços ou parentes',
                max_length=11,
                null=True,
                verbose_name='Numero de celular com o (DDD)',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='datanascimento',
            field=models.DateField(
                blank=True,
                help_text='Data de Nascimento do cliente',
                null=True,
                verbose_name='Data de nascimento',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(
                help_text='Digite o E-mail válido',
                max_length=50,
                verbose_name='E-mail de Contato',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fixo',
            field=models.CharField(
                help_text='Número Fixo apenas número Sem traços ou parentes',
                max_length=12,
                verbose_name='Numero de fixo com o (DDD)',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(
                help_text='Nome Completo do Cliente',
                max_length=80,
                verbose_name='Nome do cliente',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(
                blank=True,
                help_text='Profissão Auto Declarada do Cliente',
                max_length=80,
                null=True,
                verbose_name='Profissão do Cliente',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(
                help_text='RG Sem traços ou pontos',
                max_length=15,
                verbose_name='RG',
            ),
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
                help_text='Escolha umas das opções',
                max_length=1,
                verbose_name='Sexo',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='what',
            field=models.CharField(
                blank=True,
                help_text='Número de contato para o Whatzapp',
                max_length=11,
                null=True,
                verbose_name='Contato do Whatzapp',
            ),
        ),
    ]
