# Generated by Django 4.2.5 on 2023-09-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_property', models.CharField(max_length=6, unique=True)),
                ('limit_guests', models.IntegerField()),
                ('quantity_bathroom', models.IntegerField()),
                ('allowed_pets', models.BooleanField()),
                ('cleaning_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activation_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
