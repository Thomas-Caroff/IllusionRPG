# Generated by Django 4.2.7 on 2023-11-29 23:19

from django.db import migrations, models
import django.db.models.deletion
import utils.customUUID


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_campaign_rename_party_user_party_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='party_character',
        ),
        migrations.AddField(
            model_name='character',
            name='party_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.party'),
        ),
        migrations.AddField(
            model_name='party',
            name='character_list',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='character',
            name='items',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='guidmodel',
            name='id',
            field=models.CharField(default=utils.customUUID.custom_id, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='party_list',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='pseudo',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
