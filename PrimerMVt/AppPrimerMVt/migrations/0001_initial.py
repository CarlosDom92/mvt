# Generated by Django 4.0.3 on 2022-03-30 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('idFamiliar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=60)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('idParentesco', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=30)),
            ],
        ),
    ]
