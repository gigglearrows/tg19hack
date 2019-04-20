# Generated by Django 2.1.4 on 2019-01-27 13:59
from decimal import Decimal
from django.db import migrations

def add_items(apps, schema_editor):
    Item = apps.get_model('shop', 'Item')
    Item(sku=1, name='Horse-hair wand', price=Decimal(123.0)).save()
    Item(sku=2, name='Dragon-bone wand', price=Decimal(323.0)).save()
    Item(sku=3, name='Troll-snot wand', price=Decimal(723.0)).save()
    Item(sku=321, name='Elder Wand', price=Decimal(5000.0)).save()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_items)
    ]
