# Generated by Django 2.2.7 on 2019-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0031_person_sort_name")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="death_date",
            field=models.CharField(max_length=255, null=True),
        )
    ]
