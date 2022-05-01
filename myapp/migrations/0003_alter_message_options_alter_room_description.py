# Generated by Django 4.0.4 on 2022-05-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]