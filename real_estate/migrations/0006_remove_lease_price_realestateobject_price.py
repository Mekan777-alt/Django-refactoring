# Generated by Django 4.2.7 on 2024-01-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0005_remove_lease_address_remove_lease_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lease',
            name='price',
        ),
        migrations.AddField(
            model_name='realestateobject',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
            preserve_default=False,
        ),
    ]
