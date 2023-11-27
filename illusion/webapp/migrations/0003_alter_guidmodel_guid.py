# Generated by Django 4.2.7 on 2023-11-27 20:29

from django.db import migrations, models
import utils.customUUID


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_user_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidmodel',
            name='guid',
            field=models.UUIDField(default=utils.customUUID.custom_id, editable=False, primary_key=True, serialize=False),
        ),
    ]
