# Generated by Django 2.2.8 on 2020-02-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drop_Cv', '0006_auto_20200203_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='Message',
            field=models.CharField(max_length=255),
        ),
    ]