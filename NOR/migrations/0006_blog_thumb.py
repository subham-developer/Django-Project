# Generated by Django 2.2 on 2019-05-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOR', '0005_addresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
