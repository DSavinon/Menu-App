# Generated by Django 4.1 on 2022-09-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="alimento",
            name="imagen_alimento",
            field=models.CharField(
                default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5PTsuRj6pjDdRDNqaC27k705rxveiomd99w&usqp=CAU",
                max_length=500,
            ),
        ),
    ]
