# Generated by Django 4.2.5 on 2024-07-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_remove_produto_descricao_produto_precovenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='mao_de_obra',
            field=models.FloatField(null=True),
        ),
    ]