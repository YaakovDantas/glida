# Generated by Django 2.2.4 on 2019-08-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190818_0205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigo',
            old_name='tema',
            new_name='subTitulo',
        ),
        migrations.AddField(
            model_name='comentario',
            name='titulo',
            field=models.CharField(max_length=255, null=True, verbose_name='Nome completo do seu Abrigo/ONG'),
        ),
    ]
