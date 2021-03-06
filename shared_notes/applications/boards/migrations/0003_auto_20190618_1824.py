# Generated by Django 2.0.3 on 2019-06-18 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_auto_20190617_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=500)),
                ('approved', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=2)),
                ('type', models.CharField(choices=[('Private', 'Privado'), ('Public', 'Publico')], max_length=30)),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.CharField(choices=[('Private', 'Privado'), ('Public', 'Publico')], max_length=30),
        ),
        migrations.AddField(
            model_name='idea',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Board'),
        ),
        migrations.AddField(
            model_name='idea',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='idea_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='idea_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
