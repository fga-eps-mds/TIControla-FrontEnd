# Generated by Django 4.0.6 on 2022-07-12 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleto',
            name='valor_boleto',
        ),
    ]