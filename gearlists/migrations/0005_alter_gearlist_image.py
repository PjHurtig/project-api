# Generated by Django 3.2.20 on 2023-09-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gearlists', '0004_alter_gearlist_listtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearlist',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
