# Generated by Django 2.2 on 2019-05-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOR', '0003_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=30)),
                ('Code_Type', models.CharField(max_length=30)),
                ('value', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
