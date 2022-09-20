# Generated by Django 4.1.1 on 2022-09-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.CharField(choices=[('S', 'Spirit'), ('R', 'Sour'), ('F', 'Fizz'), ('M', 'Smash'), ('P', 'Syrup'), ('B', 'Bitters'), ('H', 'Herb'), ('J', 'Juice'), ('G', 'Garnish'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='skill_level',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1),
        ),
    ]
