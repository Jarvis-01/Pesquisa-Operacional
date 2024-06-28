# Generated by Django 5.0.6 on 2024-06-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiaPrima', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='materias_primas',
            field=models.ManyToManyField(through='produto.ProdutoMateriaPrima', to='materiaPrima.materiaprima'),
        ),
    ]
