# Generated by Django 3.2.16 on 2024-04-23 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_icecream_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
    ]
