# Generated by Django 2.2.4 on 2019-08-18 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190818_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='artigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post', to='home.Artigo'),
        ),
    ]