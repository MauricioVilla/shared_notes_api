# Generated by Django 2.0.3 on 2019-06-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20190619_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='approved',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
    ]
