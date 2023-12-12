# Generated by Django 4.2.4 on 2023-11-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstatuaSimplificada',
            fields=[
                ('nombre', models.CharField(max_length=255, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(null=True)),
                ('modelo', models.FileField(upload_to='modelos/')),
                ('ubicacion', models.TextField(null=True)),
            ],
        ),
    ]