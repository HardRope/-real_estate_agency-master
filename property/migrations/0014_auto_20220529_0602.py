# Generated by Django 2.2.24 on 2022-05-29 03:02

from django.db import migrations, models


def add_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(name=flat.flat_owner, defaults={
            'owner_phonenumber': flat.owners_phonenumber,
            'owner_pure_phone': flat.owner_pure_phone,
        })

    for flat in Flat.objects.all():
        flat_owner = Owner.objects.get(name=flat.flat_owner)
        flat_owner.flats.add(flat)
        flat_owner.save()

def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220529_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ФИО владельца')
        ),
        migrations.RunPython(add_owner, move_backward)
    ]
