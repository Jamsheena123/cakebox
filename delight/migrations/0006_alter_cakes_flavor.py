# Generated by Django 4.2.4 on 2023-11-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delight', '0005_remove_cakevarients_flavor_cakes_flavor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='flavor',
            field=models.CharField(choices=[('chocolate', 'chocolate'), ('vanilla', 'vanilla'), ('pistachio', 'pistachio'), ('tropical rum', 'tropical rum'), ('pineapple', 'pineapple'), ('red velvet', 'red velvet'), ('strawberry', 'strawberry')], default='chocolate', max_length=200),
        ),
    ]