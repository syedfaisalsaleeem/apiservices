# Generated by Django 4.0.1 on 2022-01-15 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_document_created_date_folder_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apis.folder'),
            preserve_default=False,
        ),
    ]
