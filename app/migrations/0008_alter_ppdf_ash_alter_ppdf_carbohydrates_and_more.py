# Generated by Django 4.1.2 on 2022-10-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_ppdf_water"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ppdf",
            name="ash",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ppdf",
            name="carbohydrates",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ppdf",
            name="df_insoluble",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ppdf",
            name="energy",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ppdf",
            name="protein",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ppdf",
            name="totalfat",
            field=models.FloatField(null=True),
        ),
    ]
