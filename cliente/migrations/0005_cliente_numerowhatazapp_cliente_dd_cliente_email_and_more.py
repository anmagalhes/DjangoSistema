# Generated by Django 4.1.6 on 2023-02-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_profissao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='NumeroWhatazapp',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='dd',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='fixo',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero_celula',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='situacao',
            field=models.CharField(
                choices=[('A', 'Ativo'), ('I', 'Desativado')],
                default='N',
                max_length=1,
            ),
        ),
    ]
