# Generated by Django 2.2.4 on 2019-08-18 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190818_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redator',
            old_name='nome_abrigo_completo',
            new_name='nome_completo',
        ),
    ]