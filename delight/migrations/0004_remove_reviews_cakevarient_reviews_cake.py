# Generated by Django 4.2.4 on 2023-11-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delight', '0003_rename_cakevarient_cakevarients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='cakevarient',
        ),
        migrations.AddField(
            model_name='reviews',
            name='cake',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='delight.cakes'),
        ),
    ]
