# Generated by Django 4.0.3 on 2022-04-09 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_contact_username_alter_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='problem',
        ),
    ]
