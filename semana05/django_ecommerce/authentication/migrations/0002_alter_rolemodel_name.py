# Generated by Django 5.1.2 on 2024-10-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolemodel',
            name='name',
            field=models.CharField(choices=[('ADMIN', 'Administrador'), ('SELLER', 'Vendedor')], max_length=10),
        ),
    ]
