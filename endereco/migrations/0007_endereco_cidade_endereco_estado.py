# Generated by Django 4.1.6 on 2023-02-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0006_endereco_bairro'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Cidade',
            field=models.CharField(default='', help_text='Cidade da Residencia', max_length=70, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='Estado',
            field=models.CharField(choices=[('AC', 'AC'), ('AP', 'AM'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], default='Rua', help_text='Nome do Estado', max_length=9, verbose_name='Estado'),
        ),
    ]
