# Generated by Django 4.2.7 on 2024-01-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_respuestasdos_remove_respuestas_respuesta_10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestascuatro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_28', models.CharField(max_length=255)),
                ('respuesta_29', models.CharField(max_length=255)),
                ('respuesta_30', models.CharField(max_length=255)),
                ('respuesta_31', models.CharField(max_length=255)),
                ('respuesta_32', models.CharField(max_length=255)),
                ('respuesta_33', models.CharField(max_length=255)),
                ('respuesta_34', models.CharField(max_length=255)),
                ('respuesta_35', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestastres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_19', models.CharField(max_length=255)),
                ('respuesta_20', models.CharField(max_length=255)),
                ('respuesta_21', models.CharField(max_length=255)),
                ('respuesta_22', models.CharField(max_length=255)),
                ('respuesta_23', models.CharField(max_length=255)),
                ('respuesta_24', models.CharField(max_length=255)),
                ('respuesta_25', models.CharField(max_length=255)),
                ('respuesta_26', models.CharField(max_length=255)),
                ('respuesta_27', models.CharField(max_length=255)),
            ],
        ),
    ]
