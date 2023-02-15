# Generated by Django 4.1.6 on 2023-02-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_rename_numerocpf_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=11, verbose_name='Numero de celular com o (DDD)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='datanascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fixo',
            field=models.CharField(max_length=12, verbose_name='Numero de fixo com o (DDD)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=80, verbose_name='Nome do cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Profissão do Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=15, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], default='M', max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='situacao',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=1, verbose_name='Situação do cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='what',
            field=models.CharField(max_length=11, verbose_name='Contato do Whatzapp'),
        ),
    ]
