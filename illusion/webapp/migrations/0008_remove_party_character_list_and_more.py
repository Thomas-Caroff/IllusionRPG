# Generated by Django 4.2.7 on 2023-11-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_party_party_character_character_party_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='character_list',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]
