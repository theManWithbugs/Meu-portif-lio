# Generated by Django 5.0.7 on 2024-09-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_nome_user_cpf_nome_user_data_atual'),
    ]

    operations = [
        migrations.CreateModel(
            name='NomeUser',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(max_length=80)),
                ('data_atual', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='nome_user',
        ),
    ]
