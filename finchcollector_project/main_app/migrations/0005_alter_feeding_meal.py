# Generated by Django 5.0.4 on 2024-05-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_feeding_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1),
        ),
    ]
