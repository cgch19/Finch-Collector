# Generated by Django 5.0.4 on 2024-05-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_toy_finch_toys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(related_name='finches', to='main_app.toy'),
        ),
    ]
